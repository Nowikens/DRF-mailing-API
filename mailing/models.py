from django.db import models
from django.contrib.postgres.fields import ArrayField

import uuid

# Create your models here.

class Mailbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    host = models.CharField(max_length=255)
    port = models.IntegerField(default=465)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email_from = models.CharField(max_length=255)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    @property
    def sent(self):
        return self.email_set.count()
        
    



class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    attachment = models.FileField(upload_to="uploads/", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)   
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    to = ArrayField(models.EmailField(), blank=True, null=True)
    cc = ArrayField(models.EmailField(), blank=True, null=True)
    bcc = ArrayField(models.EmailField(), blank=True, null=True)
    reply_to = models.EmailField(default=None, blank=True, null=True)
    sent_date = models.DateTimeField(default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
   
