# Generated by Django 5.1.3 on 2024-11-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.CharField(max_length=20)),
                ('reserver_name', models.CharField(max_length=100)),
                ('reserver_id', models.CharField(max_length=50)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('date', 'time_slot')},
            },
        ),
    ]
