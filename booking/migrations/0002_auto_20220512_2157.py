# Generated by Django 3.2.13 on 2022-05-12 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-booking_time']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['lname']},
        ),
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['number_of_seats']},
        ),
    ]