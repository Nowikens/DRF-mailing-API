from django.urls import path, include

from rest_framework import routers
from mailing import views

router = routers.DefaultRouter()
router.register(r'mailbox', views.MailboxViewSet)
router.register(r'template', views.TemplateViewSet)
router.register(r'email', views.EmailViewSet)
