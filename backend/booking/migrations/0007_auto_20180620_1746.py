# Generated by Django 2.0.1 on 2018-06-20 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20180620_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bokning',
            name='maskinist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
