from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.core.exceptions import ValidationError

from .models import Klient, KlientForm, Bokning, BokningForm
from .pdfMail import pdfThenMail
import json
import datetime

# Create your views here.
@ensure_csrf_cookie
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

@login_required
def logoutView(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponse(status=200)
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def bokning(request):
    if request.method == 'POST':
        klientForm = KlientForm(json.loads(request.body.decode()))
        bokningForm = BokningForm(json.loads(request.body.decode()))
        #Validera data.
        if klientForm.is_valid() and bokningForm.is_valid():
            #Skriv till db.
            namn = json.loads(request.body.decode())['namn'].strip()
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
                    return HttpResponseNotFound('<h1>User not found</h1>', user)
            bokning = bokningForm.save(commit=False)
            bokning.klient = klient
            bokning.maskinist = user
            bokning.save()
            try:
                kundmail = json.loads(request.body.decode())['kundmail'].strip()
                try:
                    #Send mail to customer if valid
                    validate_email(kundmail)
                    val = pdfThenMail(bokning, kundmail)
                except ValidationError as e:
                    return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), content_type="application/json")
            except KeyError:
                #Only send to target
                val = pdfThenMail(bokning)
            if val == True:
                return HttpResponse(status=201)
            else:
                return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(val))}), content_type="application/json")
        else:
            print(bokningForm.errors)
            return HttpResponse(status=400)
    elif request.method == 'GET':
        # Hitta User
        print('OK')
        try:
            user = getUser(request)
        except ValueError as e:
            return HttpResponseNotFound(e)
        return JsonResponse(list(Bokning.objects.filter(maskinist=user).order_by('-id')[:10].values()), safe=False)
        return JsonResponse(list(Event.objects.all().filter(product=p_id).values()), safe=False)
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
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

@login_required
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

def getUser(request):
    user = request.user
    try:
        user = User.objects.get(username=user)
    except User.DoesNotExist:
        try:
            user = User.objects.get(email=user)
        except User.DoesNotExist:
            raise ValueError('<h1>User not found</h1>')
    return user
