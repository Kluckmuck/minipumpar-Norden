from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from ..models import Klient, Bokning
import json

# Create your tests here.
## 200 (Ok) : Request was responded successfully.
## 201 (Created) : Request has created new resources successfully.
## 401 (Unauthorized) : Request requires authentication. This should be returned if you are requesting without signing in.
## 403 (Forbidden) : Request is forbidden. This should be returned if your request tries to modify resources of which you are not the owner.
## 404 (Not Found) : Requested resource is not found.
## 405 (Method not allowed) : Requested URL does not allow the method of the request.

class BokningTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        klient = Klient.objects.create(namn='Bygga AB', adress='Betonggatan 24', kontakt='Erik Betongsson')
        klient.save()
        user = User.objects.create_user(username='Korea', password='Seoul', email='bibimbap@gmail.com')
        User.objects.create_user(username='Viktor', password='Max')
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
            pumpStart='2018-07-09 13:13:13',
            pumpSlut='2018-07-09 13:13:13'
        )

        cls.client = Client()

    def test_auth(self):
        response = self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/logout/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/api/login/', json.dumps({'username': 'Badder', 'password': 'Nabber'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)

        #Redirects pga. att använder inte är inloggad
        response = self.client.get('/api/bokning/1/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/api/klient/1/')
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/api/bokning/')

    def test_passwordChange(self):
        self.client.post('/api/login/', json.dumps({'username': 'Viktor', 'password': 'Max'}), content_type='application/json')
        response = self.client.post('/api/change-password/')
        self.assertEqual(response.status_code, 200)

    def test_getKlient(self):
        login_auth(self) #Login för @login_required
        #Hämta Klient 1
        response = self.client.get('/api/klient/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Klient.objects.get(id=1).namn, 'Bygga AB')
        self.assertEqual(Klient.objects.get(id=1).adress, 'Betonggatan 24')

        #Hämta en klient som inte finns
        response = self.client.get('/api/klient/99/')
        self.assertEqual(response.status_code, 404)

    def test_getBokning(self):
        login_auth(self) #Login för @login_required
        response = self.client.get('/api/bokning/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Bokning.objects.get(id=1).pumpMng, 20)
        self.assertEqual(Bokning.objects.get(id=1).ovrigInfo, "")

        # Icke existerande bokning
        response = self.client.get('/api/bokning/123/')
        self.assertEqual(response.status_code, 404)

    def test_postBokning(self):
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
            'pumpStart' : '2018-06-11 13:13:21',
            'pumpSlut' : '2018-06-11 13:13:21'
        }), content_type='application/json')

        response2 = self.client.post('/api/bokning/', json.dumps({
            'namn': 'Bygga AB',
            'adress':'Betonggatan 24',
            'kontakt' :'Erik Betongsson',
            'pumpMng': '1233',
            'littNr': ' 31A42  ',
            'resTid': '5',
            'maskinist': 'bibimbap@gmail.com',
            'grundavgift' : '1250',
            'datum' : '2018-06-12',
            'pumpStart' : '2018-06-12 14:13:21',
            'pumpSlut' : '2018-06-12 10:13:21'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response2.status_code, 201)

        self.assertEqual(Klient.objects.get(id=1).namn, 'Bygga AB')
        #White spaces should be removed
        self.assertEqual(Klient.objects.get(id=2).namn, 'Minipump AB')
        self.assertEqual(Klient.objects.get(id=2).adress, 'Pumpgatan 20')

        #Bokning 2 ska ej modifieras
        self.assertEqual(Bokning.objects.get(id=2).resTid, 4)
        self.assertEqual(Bokning.objects.get(id=2).pumpMng, 13)
        self.assertEqual(Bokning.objects.get(id=2).ovrigInfo, '')

        #Bokning 3
        self.assertEqual(Bokning.objects.get(id=3).pumpMng, 1233)
        self.assertEqual(Bokning.objects.get(id=3).ovrigInfo, '')
        #White spaces should be removed
        self.assertEqual(Bokning.objects.get(id=3).littNr, '31A42')

        # Maskinist tests
        self.assertEqual(Bokning.objects.get(id=2).maskinist, User.objects.get(id=1))
        self.assertEqual(Bokning.objects.get(id=3).maskinist, User.objects.get(id=1))

        #Testar att klient 3 inte existerar
        response = self.client.get('/api/klient/3/')
        self.assertEqual(response.status_code, 404)

def login_auth(self):
    self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')
