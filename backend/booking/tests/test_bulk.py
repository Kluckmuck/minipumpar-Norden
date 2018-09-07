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

class BulkTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Testing with many boknings
        klient = Klient.objects.create(namn='Bygga AB', adress='Betonggatan 24', kontakt='Erik Betongsson')
        klient.save()
        user = User.objects.create_user(username='Korea', password='Seoul', email='bibimbap@gmail.com')
        user2 = User.objects.create_user(username='Svergie', password='gbg11123', email='semla@gmail.com')
        User.objects.create_user(username='Viktor', password='Max')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-09', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-11', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-13', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-15', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-17', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-19', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-21', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user2, ovrigInfo='', datum='2018-07-23', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user, ovrigInfo='', datum='2018-07-25', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')
        Bokning.objects.create(klient=klient, pumpMng='20', littNr='1234', resTid='2', grundavgift='1000', slangStr=None, maskinist=user2, ovrigInfo='', datum='2018-07-27', pumpStart='2018-07-09 13:13:13', pumpSlut='2018-07-09 13:13:13')

        cls.client = Client()

    def test_getLatestBoknings(self):
        login_auth(self) #Login för @login_required
        response = self.client.get('/api/bokning/')
        self.assertEqual(response.status_code, 200)
        print(response.content)
        self.assertEqual(response.content, 'Hej')

def login_auth(self):
    self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')
