# Generated by Django 3.2.13 on 2022-05-14 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['last_name']},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='lname',
            new_name='last_name',
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_size', models.IntegerField()),
                ('time_of_booking', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='booking.customer')),
                ('tables', models.ManyToManyField(related_name='bookings', to='booking.Table')),
            ],
        ),
    ]