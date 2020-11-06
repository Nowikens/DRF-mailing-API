from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend

from .models import Mailbox, Template, Email
from .serializers import MailboxSerializer, TemplateSerializer, EmailSerializer
from .filters import EmailFilter
from .task import celery_email

# Create your views here.

class MailboxViewSet(viewsets.ModelViewSet):
    
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer
    
    # This is to avoid csrf "CSRF Failed: CSRF token missing or incorrect." error when using postman
    permission_classes = ()
    authentication_classes = ()
    def retrieve(self, request, pk=None):
        try:
            queryset = Mailbox.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MailboxSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)




class TemplateViewSet(viewsets.ModelViewSet):
    
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    
    permission_classes = ()
    authentication_classes = ()
    def retrieve(self, request, pk=None):
        
        try:
            queryset = Template.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TemplateSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)



class EmailViewSet(viewsets.ModelViewSet):
    
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EmailFilter
    
    allowed_methods = ['GET', 'POST']
    permission_classes = ()
    authentication_classes = ()
    
    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_403_FORBIDDEN)
            
    def create(self, request, *args, **kwargs):
    
        if Mailbox.objects.get(pk=request.data['mailbox']).is_active == False:
            return Response(
            {'Mailbox is inactive': 'use active mailbox'}, 
            status=status.HTTP_403_FORBIDDEN)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        celery_email.delay(serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    


