# Generated by Django 4.1 on 2022-08-13 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_agent_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='logo',
        ),
    ]
