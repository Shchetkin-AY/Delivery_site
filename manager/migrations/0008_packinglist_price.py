# Generated by Django 4.1 on 2022-08-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_remove_agent_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='packinglist',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]