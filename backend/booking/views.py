from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, requires_csrf_token

from .models import Klient, KlientForm, Bokning, BokningForm
import json
import datetime

# Create your views here.
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

def logoutView(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['GET'])

def bokning(request):
    if request.method == 'POST':
        klientForm = KlientForm(json.loads(request.body.decode()))
        bokningForm = BokningForm(json.loads(request.body.decode()))
        #Validera data.
        if klientForm.is_valid() and bokningForm.is_valid():
            #Skriv till db.
            klient = klientForm.save()
            bokning = bokningForm.save(commit=False)
            bokning.klient = klient
            bokning.save()
            return HttpResponse(status=201)
        else:
            print(klientForm.errors.as_json())
            return HttpResponse(status=400)
    else:
        return HttpResponseNotAllowed(['POST'])

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
