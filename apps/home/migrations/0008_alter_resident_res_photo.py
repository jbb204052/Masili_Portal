# Generated by Django 3.2.16 on 2022-11-13 03:33

import apps.home.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_resident_res_isvoter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='res_photo',
            field=models.ImageField(blank=True, null=True, storage=apps.home.storage.OverwriteStorage(), upload_to=None),
        ),
    ]
