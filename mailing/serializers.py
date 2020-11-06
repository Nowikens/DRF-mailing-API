from .models import Mailbox, Template, Email
from rest_framework import serializers


class MailboxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mailbox
        fields = '__all__'
        read_only_fields = ['date', 'last_update']
        write_only = ['login', 'password']



class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'
        read_only_fields = ['date', 'last_update']
        

class EmailSerializer(serializers.ModelSerializer):
    to = serializers.ListField(child=serializers.EmailField(allow_blank=True, allow_null=True))
    cc = serializers.ListField(child=serializers.EmailField(allow_blank=True, allow_null=True))
    bcc = serializers.ListField(child=serializers.EmailField(allow_blank=True, allow_null=True))
    class Meta:
        model = Email
        fields = '__all__'
        read_only_fields = ['sent_date', 'date']
