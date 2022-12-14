# Generated by Django 3.2.16 on 2022-11-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brgy_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brgy_name', models.CharField(max_length=50)),
                ('brgy_city', models.CharField(max_length=50)),
                ('brgy_province', models.CharField(max_length=50)),
                ('brgy_contactNo', models.CharField(max_length=11)),
                ('brgy_email', models.EmailField(max_length=50)),
                ('brgy_logo', models.ImageField(blank=True, default='brgy_info/default.png', upload_to='brgy_info/')),
                ('brgy_history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('res_fname', models.CharField(max_length=50)),
                ('res_lname', models.CharField(max_length=50)),
                ('res_mname', models.CharField(blank=True, max_length=50)),
                ('res_extname', models.CharField(blank=True, max_length=5)),
                ('res_gender', models.CharField(choices=[['MALE', 'MALE'], ['FEMALE', 'FEMALE']], max_length=10)),
                ('res_bdate', models.DateField()),
                ('res_place_of_birth', models.CharField(max_length=50)),
                ('res_address', models.CharField(max_length=100)),
                ('res_contactNo', models.CharField(max_length=11)),
                ('res_email', models.EmailField(max_length=50)),
                ('res_civil_status', models.CharField(choices=[['SINGLE', 'SINGLE'], ['MARRIED', 'MARRIED'], ['WIDOWED', 'WIDOWED'], ['SEPARATED', 'SEPARATED'], ['DIVORCED', 'DIVORCED']], max_length=10)),
                ('res_occupation', models.CharField(max_length=50)),
                ('res_educ_attainment', models.CharField(max_length=50)),
                ('res_nationality', models.CharField(max_length=50)),
                ('res_religion', models.CharField(max_length=50)),
            ],
        ),
    ]
