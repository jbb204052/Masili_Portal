# Generated by Django 3.2.16 on 2022-11-13 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_purok_purok_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resident',
            old_name='res_address',
            new_name='res_address1',
        ),
        migrations.AddField(
            model_name='resident',
            name='res_purok',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.purok'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brgy_info',
            name='brgy_contactNo',
            field=models.CharField(max_length=11),
        ),
    ]
