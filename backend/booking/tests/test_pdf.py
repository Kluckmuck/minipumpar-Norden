from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core import mail

from ..models import Klient, Bokning
import json

# Create your tests here.
## 200 (Ok) : Request was responded successfully.
## 201 (Created) : Request has created new resources successfully.
## 401 (Unauthorized) : Request requires authentication. This should be returned if you are requesting without signing in.
## 403 (Forbidden) : Request is forbidden. This should be returned if your request tries to modify resources of which you are not the owner.
## 404 (Not Found) : Requested resource is not found.
## 405 (Method not allowed) : Requested URL does not allow the method of the request.

class PdfTestCase(TestCase):
    def setUp(self):
        klient = Klient.objects.create(namn='Bygga AB', adress='Betonggatan 24', kontakt='Erik Betongsson')
        user = User.objects.create_user(username='Korea', password='Seoul', email='bibimbap@gmail.com')
        bokning = Bokning.objects.create(
            klient=klient,
            pumpMng='20',
            littNr='1234',
            resTid='2',
            grundavgift='1000',
            slangStr=None,
            maskinist=user,
            ovrigInfo='',
            datum='2018-07-09',
            pumpStart='2018-07-09 13:00:13',
            pumpSlut='2018-07-09 14:15:13'
        )

        self.client = Client()

    def test_send_email(self):
        login_auth(self) #Login för @login_required
        # Send message.
        response = self.client.post('/api/mail/', json.dumps({'bokning': '1', 'recipient': 'kluckmucki@gmail.com', 'sender': 'max.jourdanis@gmail.com'}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'subject')
        # Veryfy attachment
        self.assertEqual(mail.outbox[0].attachments[0][0], 'bookning.pdf')

        # POST without recipient field
        response = self.client.post('/api/mail/', json.dumps({'bokning': '1', 'user': 'max.jourdanis@gmail.com'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # POST with blank recipient
        response = self.client.post('/api/mail/', json.dumps({'bokning': '1', 'recipient': '', 'user': 'max.jourdanis@gmail.com'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_pdfBokning(self):
        login_auth(self) #Login för @login_required
        response = self.client.get('/api/pdf/bokning/1/')
        self.assertEqual(response.status_code, 201)

def login_auth(self):
    self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')
