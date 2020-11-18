from rest_framework.test import APITestCase

from mailing.models import Mailbox, Template, Email

# Create your tests here.
def tearDownModule():
    pass
class UrlsTestCase(APITestCase):
    """Testing url routes responses"""

    def setUp(self):
        self.mailbox = Mailbox.objects.create(
            host = "superhost",
            port = 465,
            login = "login",
            password = "password",
            email_from = "email@from.com"

        )

        self.template = Template.objects.create(
            subject = "subject",
            text = "text"
        )

        self.email = Email.objects.create(
            mailbox = self.mailbox,
            template = self.template,
            to = ["email@to.com"]
        )

    def test_homepage(self):
        """There is no homepage"""
        request = self.client.get('/')
        self.assertEqual(request.status_code, 404)

    def test_api(self):
        request = self.client.get('/api/')
        self.assertEqual(request.status_code, 200)


    def test_mailbox_list(self):
        request = self.client.get('/api/mailbox/')
        self.assertEqual(request.status_code, 200)

    def test_mailbox_detail(self):
        request = self.client.get(f'/api/mailbox/{self.mailbox.id}/')
        self.assertEqual(request.status_code, 200)


    def test_template_list(self):
        request = self.client.get('/api/template/')
        self.assertEqual(request.status_code, 200)

    def test_template_detail(self):
        request = self.client.get(f'/api/template/{self.template.id}/')
        self.assertEqual(request.status_code, 200)


    def test_email_list(self):
        request = self.client.get('/api/email/')
        self.assertEqual(request.status_code, 200)

    def test_email_detail(self):
        """Email detail is forbidden"""
        request = self.client.get(f'/api/email/{self.email.id}/')
        self.assertEqual(request.status_code, 403)
