from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound
from django.forms.models import model_to_dict
from django.utils import timezone

from .models import Klient, KlientForm, Bokning, BokningForm
import json
import datetime

# Create your views here.
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
    elif request.method == 'GET':
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def klient(request, klientId):
    if request.method == 'GET':
        id = int(klientId)
        try:
            klient = Klient.objects.get(id=id)
        except Klient.DoesNotExist:
            return HttpResponseNotFound()
        return JsonResponse(model_to_dict(klient))
