from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from datetime import datetime

# Create your models here.
class Klient(models.Model):
    namn = models.CharField(max_length=124)
    adress = models.CharField(max_length=124)
    kontakt = models.CharField(max_length=124)

    def __str__(self):
       return self.namn + " vid " + self.adress + ", " + self.kontakt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    targetMail = models.EmailField(default='info@minipumpar.se')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ['namn', 'adress', 'kontakt']

class BokningForm(forms.ModelForm):
    pumpStart = forms.DateTimeField(input_formats=['%H:%M'])
    pumpSlut = forms.DateTimeField(input_formats=['%H:%M'])
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
