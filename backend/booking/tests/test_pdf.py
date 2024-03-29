from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core import mail
import os

from ..models import Klient, Bokning
from ..pdfMail import createPdf

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
        user.profile.targetMail = 'kluckmucki@gmail.com'
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
        Bokning.objects.create(
            klient=klient,
            pumpMng='20',
            littNr='1234',
            resTid='2',
            grundavgift='1000',
            slangStr=None,
            maskinist=user,
            ovrigInfo='Extra tungt idag!',
            datum='2017-03-04',
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
            'pumpStart' : '00:02',
            'pumpSlut' : '00:02'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(os.path.exists('2018-06-11(2)'), False)

    def test_createPdf(self):
        #Create two PDFs. Test if they both look ok!
        createPdf(Bokning.objects.get(id=1))
        createPdf(Bokning.objects.get(id=2))

    def test_pdfBokningTwoMail(self):
        login_auth(self) #Login för @login_required
        response = self.client.post('/api/bokning/', json.dumps({
            'namn': '  Bygga Mer HB   ',
            'adress':'Vasagatan 17    ',
            'kontakt' :'Karl Karlsson',
            'pumpMng': '15',
            'littNr': '134 5C',
            'resTid': '2',
            'grundavgift' : '3000',
            'datum' : '2018-02-17',
            'pumpStart' : '12:00',
            'pumpSlut' : '16:45',
            'kundmail' : 'viktor.karl.lundberg@gmail.com'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

def login_auth(self):
    self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')
