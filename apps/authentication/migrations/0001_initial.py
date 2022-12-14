# Generated by Django 3.2.16 on 2022-11-11 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_pics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, default='profile_pics/default.png', upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
