# Generated by Django 4.1.1 on 2022-09-08 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='password',
        ),
    ]
