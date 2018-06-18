from django.test import TestCase, Client
from ..models import Klient, Bokning
from django.contrib.auth.models import User
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
        bokning = Bokning.objects.create(
            klient=klient,
            pumpMng='20',
            littNr='1234',
            resTid='2',
            grundavgift='1000',
            referens=None,
            pumpStr=None,
            slangStr=None,
            pump=None,
            maskinist='',
            betongLev='',
            betongKvalite='',
            bestalld=None,
            arbNr=None,
            ovrigInfo='',
            datum='2018-07-09',
            pumpStart='2018-07-09 13:13:13',
            pumpSlut='2018-07-09 13:13:13'
        )
        User.objects.create_user(username='Korea', password='Seoul')
        self.client = Client()

    def test_pdfBokning(self):
        login_auth(self) #Login för @login_required
        response = self.client.get('/api/pdf/bokning/1/')
        self.assertEqual(response.status_code, 201)

def login_auth(self):
    self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')