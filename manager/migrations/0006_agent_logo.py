# Generated by Django 4.1 on 2022-08-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_packinglist_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='logo',
            field=models.ImageField(null=True, upload_to='MEDIA_COMPANY_IMAGE_DIR'),
        ),
    ]