# Generated by Django 2.0.6 on 2018-08-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20180806_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bokning',
            name='pumpMng',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Pump mängd'),
        ),
    ]
