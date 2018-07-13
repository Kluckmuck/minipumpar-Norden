from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core.exceptions import ValidationError
from django.db import connection
from reportlab.pdfgen import canvas

from .models import Klient, KlientForm, Bokning, BokningForm
import json
import datetime

# Create your views here.
@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        username = json.loads(request.body.decode())['username']
        password = json.loads(request.body.decode())['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200) #OK
        else:
            return HttpResponse(status=401) #DENIED
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def logoutView(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def bokning(request):
    if request.method == 'POST':
        klientForm = KlientForm(json.loads(request.body.decode()))
        bokningForm = BokningForm(json.loads(request.body.decode()))
        #Validera data.
        try:
            klientForm.is_valid()
            bokningForm.is_valid()
        except ValidationError as e:
            return HttpResponse(e, status=400)
        #Skriv till db.
        namn = json.loads(request.body.decode())['namn'].strip()
        #user = json.loads(request.body.decode())['maskinist'].strip()
        user = request.user
        # Se om en instans av Klient finns i DB
        query = Klient.objects.filter(namn=namn)
        if query.exists():
            klient = Klient.objects.get(namn=namn)
        else:
            klient = klientForm.save()
        # Hitta User
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=user)
            except User.DoesNotExist:
                return HttpResponseNotFound('<h1>User not found</h1>')
        bokning = bokningForm.save(commit=False)
        bokning.klient = klient
        bokning.maskinist = user
        bokning.save()
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def getBokning(request, bokningId):
    if request.method == 'GET':
        id = int(bokningId)
        try:
            bokning = Bokning.objects.get(id=id)
        except Bokning.DoesNotExist:
            return HttpResponseNotFound()
        return JsonResponse(model_to_dict(bokning))
    else:
        return HttpResponseNotAllowed(['GET'])

@csrf_exempt
def klient(request, klientId):
    if request.method == 'GET':
        id = int(klientId)
        try:
            klient = Klient.objects.get(id=id)
        except Klient.DoesNotExist:
            return HttpResponseNotFound()
        return JsonResponse(model_to_dict(klient))
    else:
        return HttpResponseNotAllowed(['GET'])

@ensure_csrf_cookie
def token(request):
    if request.method == 'GET':
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET'])
