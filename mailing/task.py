from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from django.utils import timezone

from smtplib import SMTPException

from mailing.models import Email

from celery import shared_task


@shared_task()
def celery_email(email_id):
    
    email_object = Email.objects.get(pk=email_id)
    
    # Set django mail setting based on mailbox object
    backend = EmailBackend(host=email_object.mailbox.host,
                            port=email_object.mailbox.port,
                            username=email_object.mailbox.login,
                            password=email_object.mailbox.password,
                            use_ssl=email_object.mailbox.host)
    
    # Create Email Message
    email = EmailMessage(
        subject=email_object.template.subject,
        body=email_object.template.text,
        from_email=email_object.mailbox.email_from,
        to=email_object.to,
        bcc=email_object.bcc,
        cc=email_object.cc,
        reply_to=[email_object.reply_to], # Without brackets celery gives error: 'TypeError: "reply_to" argument must be a list or tuple'
        connection=backend
        
    )
    # add attachment if there is any
    if email_object.template.attachment:
        email.attach_file(email_object.template.attachment.path)
    
    try:
        email.send(fail_silently=False)
    except SMTPException as e:
        logger.error(e)
        
        raise celery_email.retry(exc=e, max_retries=2, countdown=60)
    
    # Email was sent, set sent_date and save
    email_object.sent_date = timezone.now()
    email_object.save()
    return None