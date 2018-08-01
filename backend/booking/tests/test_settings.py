from django.test import TestCase, Client
from django.contrib.auth.models import User
import json

# Create your tests here.
## 200 (Ok) : Request was responded successfully.
## 201 (Created) : Request has created new resources successfully.
## 401 (Unauthorized) : Request requires authentication. This should be returned if you are requesting without signing in.
## 403 (Forbidden) : Request is forbidden. This should be returned if your request tries to modify resources of which you are not the owner.
## 404 (Not Found) : Requested resource is not found.
## 405 (Method not allowed) : Requested URL does not allow the method of the request.

class SettingsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='Korea', password='Seoul', email='bibimbap@gmail.com')
        cls.client = Client()

    def test_targetMail(self):
        self.assertEqual(User.objects.get(id=1).profile.targetMail, 'info@minipumpar.se')

    def test_postTargetMail(self):
        login_auth(self) #Login för @login_required och för att veta av användaren
        response = self.client.post('/api/settings/targetMail/', json.dumps({'email': 'kluckmucki@gmail.com'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.get(id=1).profile.targetMail, 'kluckmucki@gmail.com')

    def test_postBadTargetMail(self):
        login_auth(self) #Login för @login_required och för att veta av användaren
        response = self.client.post('/api/settings/targetMail/', json.dumps({'email': 'kluckmucki.gmail.com'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/api/settings/targetMail/', json.dumps({'email': 'kluckmucki@gmail'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/api/settings/targetMail/', json.dumps({'maiasdasdl': 'kluckmucki@gmail.com'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_getUserInfo(self):
        login_auth(self) #Login för @login_required och för att veta av användaren
        response = self.client.get('/api/settings/user/')
        self.assertEqual(response.status_code, 200)


def login_auth(self):
    self.client.post('/api/login/', json.dumps({'username': 'Korea', 'password': 'Seoul'}), content_type='application/json')
