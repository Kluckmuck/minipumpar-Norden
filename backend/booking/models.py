from django.db import models
from django.utils import timezone

# Create your models here.
class Klient(models.Model):
    namn = models.CharField(max_length=124)
    adress = models.CharField(max_length=124)
    kontakt = models.CharField(max_length=124)

    def __str__(self):
       return self.namn

class Bookning(models.Model):
    klient = models.ForeignKey('Klient', on_delete=models.CASCADE)
    pumpStr = models.IntegerField(blank=True, null=True)
    slangStr = models.IntegerField(blank=True, null=True)
    pump = models.IntegerField(blank=True, null=True)
    maskinist = models.CharField(max_length=124)
    betongLev = models.CharField(max_length=124)
    betongKvalite = models.CharField(max_length=124)
    bestalld = models.IntegerField()
    pumpMng = models.IntegerField()
    datum = models.DateTimeField(default=timezone.now)
    littNr = models.IntegerField()
    arbNr = models.IntegerField()
    resTid = models.IntegerField()
    grundavgift = models.IntegerField()
    pumpStart = models.DateTimeField(default=timezone.now)
    pumpSlut = models.DateTimeField(default=timezone.now)
    ovrigInfo = models.CharField(max_length=124)

    def __str__(self):
       return self.klient.namn + " vid " + self.klient.adress + ", " + self.datum
