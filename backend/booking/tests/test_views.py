from django.test import TestCase, Client
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
            pumpStart='2018-07-09 13:13:13',
            pumpSlut='2018-07-09 13:13:13'
        )

        self.client = Client()

    def test_getKlient(self):
        #Hämta Klient 1
        response = self.client.get('/api/klient/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Klient.objects.get(id=1).namn, 'Bygga AB')
        self.assertEqual(Klient.objects.get(id=1).adress, 'Betonggatan 24')

        #Hämta en klient som inte finns
        response = self.client.get('/api/klient/99/')
        self.assertEqual(response.status_code, 404)

    def test_postKlient(self):
        #Posta minimal bokning
        response = self.client.post('/api/bokning/', json.dumps({
            'namn': 'Minipump AB',
            'adress':'Pumpgatan 20',
            'kontakt' :'Zara Larsson',
            'pumpMng': '13',
            'littNr': '3144',
            'resTid': '4',
            'grundavgift' : '1500',
            'datum' : '2018-06-11',
            'pumpStart' : '2018-06-11 13:13:21',
            'pumpSlut' : '2018-06-11 13:13:21'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Klient.objects.get(id=2).namn, 'Minipump AB')
        self.assertEqual(Bokning.objects.get(id=2).pumpMng, 13)
        self.assertEqual(Bokning.objects.get(id=2).arbNr, None)
