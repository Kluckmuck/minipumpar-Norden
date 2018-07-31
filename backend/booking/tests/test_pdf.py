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
    @classmethod
    def setUpTestData(cls):
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

        cls.client = Client()

    def test_pdfBokning(self):
        login_auth(self) #Login för @login_required
        #Posta minimal bokning
        response = self.client.post('/api/bokning/', json.dumps({
            'namn': '  Minipump AB   ',
            'adress':'Pumpgatan 20    ',
            'kontakt' :'Zara Larsson',
            'pumpMng': '13',
            'littNr': '3144',
            'resTid': '4',
            'grundavgift' : '1500',
            'datum' : '2018-06-11',
            'pumpStart' : '2019-01-01T00:02',
            'pumpSlut' : '2019-02-01T00:02'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

def login_auth(self):
    self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')
