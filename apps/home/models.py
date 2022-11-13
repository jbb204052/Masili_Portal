# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from django.db import models
from django.contrib.auth.models import User
from . import storage

# Create your models here.

def resPhoto_path():
    def _func(instance, filename):
        return os.path.join('resident', str(instance.id) + '.png')
    return _func


def logo_path(path):
    def _func(instance, filename):
        return os.path.join(path, 'logo' + '.png')
    return _func


class Resident(models.Model):
    id = models.AutoField(primary_key=True)
    res_fname = models.CharField(max_length=50, blank=False)
    res_lname = models.CharField(max_length=50, blank=False)
    res_mname = models.CharField(max_length=50, blank=True)
    res_extname = models.CharField(max_length=5, blank=True)
    gender = (
        ['MALE', 'MALE'],
        ['FEMALE', 'FEMALE']
    )
    res_gender = models.CharField(max_length=10, choices=gender, blank=False)
    res_bdate = models.DateField(blank=False)
    res_place_of_birth = models.CharField(max_length=50, blank=False)
    res_purok = models.ForeignKey('purok', on_delete=models.CASCADE, blank=False)
    res_address1 = models.CharField(max_length=100, blank=False)
    res_contactNo = models.CharField(max_length=11, blank=False)
    res_email = models.EmailField(max_length=50, blank=False)
    civil_status = (
        ['SINGLE', 'SINGLE'],
        ['MARRIED', 'MARRIED'],
        ['WIDOWED', 'WIDOWED'],
        ['SEPARATED', 'SEPARATED'],
        ['DIVORCED', 'DIVORCED']
    )
    res_civil_status = models.CharField(max_length=10, choices=civil_status, blank=False)
    res_occupation = models.CharField(max_length=50, blank=False)
    res_nationality = models.CharField(max_length=50, blank=False)
    res_religion = models.CharField(max_length=50, blank=False)
    res_photo = models.ImageField(upload_to=resPhoto_path(), blank=True, null=True, storage=storage.OverwriteStorage())
    voter=(('YES','YES'),('NO','NO'))
    res_isVoter = models.CharField(max_length=10, choices=voter, blank=False)

    def __str__(self):
        return str(self.id)


class brgy_info(models.Model):
    id = models.AutoField(primary_key=True)
    brgy_name = models.CharField(max_length=50, blank=False)
    brgy_city = models.CharField(max_length=50, blank=False)
    brgy_province = models.CharField(max_length=50, blank=False)
    brgy_contactNo = models.CharField(max_length=11, blank=False)
    brgy_email = models.EmailField(max_length=50, blank=False)
    brgy_logo = models.ImageField(storage=storage.OverwriteStorage, upload_to=logo_path('brgy_info/'), default='brgy_info/default.png')
    brgy_history = models.TextField(blank=False)

    def __str__(self):
        return self.brgy_name

    def save(self, *args, **kwargs):
        if brgy_info.objects.count() > 0:
            self.pk = brgy_info.objects.first().pk
        return super(brgy_info, self).save(*args, **kwargs)

class purok(models.Model):
    id = models.AutoField(primary_key=True)
    purok_name = models.CharField(max_length=50, blank=False, unique=True)
    purok_description = models.TextField(blank=True)

    def __str__(self):
        return self.purok_name