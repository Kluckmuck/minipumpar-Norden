from django.shortcuts import render

from .models import Klient, Booking

import json
# Create your views here.

def bookning(request):
    if request.method == 'POST':
