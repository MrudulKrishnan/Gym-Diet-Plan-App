# Generated by Django 3.2.20 on 2023-10-10 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gym_diet_plan_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='TRAINER_ID',
        ),
    ]
