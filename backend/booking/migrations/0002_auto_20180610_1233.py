# Generated by Django 2.0.6 on 2018-06-10 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bokning',
            name='arbNr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bokning',
            name='bestalld',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bokning',
            name='pump',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bokning',
            name='pumpStr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bokning',
            name='referens',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bokning',
            name='slangStr',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
