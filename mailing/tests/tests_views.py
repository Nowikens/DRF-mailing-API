from rest_framework.test import APITestCase

from unittest import skip

from mailing.models import Mailbox, Template, Email

# Create your tests here.

class MailboxTestCase(APITestCase):
    """Testing creating objects through views"""
    def setUp(self):

        self.mailbox_data = {
            "host": "superhost",
            "port": 465,
            "login": "login",
            "password": "password",
            "email_from": "email@from.com"
        }

        self.template_data = {
            "subject": "subject",
            "text": "text"
        }

        self.email_data = {
            "mailbox": 00000000-0000-0000-0000-000000000000,
            "template": 00000000-0000-0000-0000-000000000000,
            "to": ["email@to.com"]
        }



    def test_create_mailbox(self):
        request = self.client.post('/api/mailbox/', self.mailbox_data, format='json')
        self.assertEqual(request.status_code, 201)
        self.assertEqual(request.data['host'], self.mailbox_data['host'])

    def test_create_template(self):
        request = self.client.post('/api/template/', self.template_data, format='json')
        self.assertEqual(request.status_code, 201)
        self.assertEqual(request.data['subject'], self.template_data['subject'])

    def test_create_email_inactive_mailbox(self):
        Mailbox.objects.create(id=0)
        Template.objects.create(id=0)
        request = self.client.post('/api/email/', self.email_data, format='json')
        self.assertEqual(request.status_code, 403)
        self.assertEqual(request.data, {'Mailbox is inactive': 'use active mailbox'})


    def test_create_email_active_mailbox(self):
        """Running Redis is required to completethis this test"""
        Mailbox.objects.create(id=0, is_active=True)
        Template.objects.create(id=0)
        request = self.client.post('/api/email/', self.email_data, format='json')
        self.assertEqual(request.status_code, 201)
        self.assertEqual(request.data['to'], self.email_data['to'])
        self.assertEqual(request.data['cc'], [])
