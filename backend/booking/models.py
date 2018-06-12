from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class Klient(models.Model):
    namn = models.CharField(max_length=124)
    adress = models.CharField(max_length=124)
    kontakt = models.CharField(max_length=124)

    def __str__(self):
       return self.namn + " vid " + self.adress + ", " + self.kontakt

class Bokning(models.Model):
    klient = models.ForeignKey('Klient', on_delete=models.CASCADE)
    referens = models.IntegerField(null=True, blank=True)
    pumpStr = models.IntegerField(null=True, blank=True)
    slangStr = models.IntegerField(null=True, blank=True)
    pump = models.IntegerField(null=True, blank=True)
    maskinist = models.CharField(max_length=124, blank=True)
    betongLev = models.CharField(max_length=124, blank=True)
    betongKvalite = models.CharField(max_length=124, blank=True)
    bestalld = models.IntegerField(null=True, blank=True)
    pumpMng = models.IntegerField()
    datum = models.DateField()
    littNr = models.IntegerField()
    arbNr = models.IntegerField(null=True, blank=True)
    resTid = models.IntegerField()
    grundavgift = models.IntegerField()
    pumpStart = models.DateTimeField()
    pumpSlut = models.DateTimeField()
    ovrigInfo = models.CharField(max_length=124, blank=True)

    def __str__(self):
       return self.klient.namn + " vid " + self.klient.adress + ", " + self.datum

class KlientForm(ModelForm):
    class Meta:
        model = Klient
        fields = ['namn', 'adress', 'kontakt']

class BokningForm(ModelForm):
    class Meta:
        model = Bokning
        fields = [
            'referens',
            'pumpStr',
            'slangStr',
            'pump',
            'maskinist',
            'betongLev',
            'betongKvalite',
            'bestalld',
            'pumpMng',
            'datum',
            'littNr',
            'arbNr',
            'resTid',
            'grundavgift',
            'pumpStart',
            'pumpSlut',
            'ovrigInfo']
