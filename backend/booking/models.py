from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Klient(models.Model):
    namn = models.CharField(max_length=124)
    adress = models.CharField(max_length=124)
    kontakt = models.CharField(max_length=124)

    def __str__(self):
       return self.namn + " vid " + self.adress + ", " + self.kontakt

class Bokning(models.Model):
    klient = models.ForeignKey('Klient', on_delete=models.CASCADE)
    slangStr = models.IntegerField(null=True, blank=True)
    maskinist = models.ForeignKey(User, on_delete=models.CASCADE)
    pumpMng = models.IntegerField()
    datum = models.DateField()
    littNr = models.CharField(max_length=124)
    resTid = models.IntegerField()
    grundavgift = models.IntegerField()
    pumpStart = models.DateTimeField()
    pumpSlut = models.DateTimeField()
    ovrigInfo = models.CharField(max_length=124, blank=True)

    def __str__(self):
       return self.klient.namn + " vid " + self.klient.adress + ", " + str(self.datum)

class KlientForm(ModelForm):
    class Meta:
        model = Klient
        fields = ['namn', 'adress', 'kontakt']

class BokningForm(ModelForm):
    class Meta:
        model = Bokning
        fields = [
            'slangStr',
            'pumpMng',
            'datum',
            'littNr',
            'resTid',
            'grundavgift',
            'pumpStart',
            'pumpSlut',
            'ovrigInfo']
