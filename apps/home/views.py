# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from . import forms, models
from django.contrib import messages
from tablib import Dataset
from .resources import *
from datetime import date

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def brgy_info(request):
    _data = models.brgy_info.objects.first()
    form = forms.BrgyInfoForm
    context = {'form': form, 'segment': {'brgy_info', 'general'}}
    if request.method == 'POST':
        form = forms.BrgyInfoForm(request.POST, request.FILES)
        # context['form'] = form
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Brgy Info updated successfully')
            return redirect('brgy_info')
        else:
            messages.error(request, 'Error updating Brgy Info')
    else:
        form = forms.BrgyInfoForm(instance=_data)
        context = {'form': form, 'segment': {'brgy_info', 'general'}, 'data': _data}
    html_template = loader.get_template('home/brgy_info.html')
    return HttpResponse(html_template.render(context, request))

# PUROK
def brgy_purok(request, id=0):
    _data = models.purok.objects.all()
    # form = forms.BrgyPurok()
    context = { 'segment': {'brgy_info', 'purok'}, 'data': _data}
    html_template = loader.get_template('home/purok/brgy_purok.html')
    return HttpResponse(html_template.render(context, request))

def brgy_purok_add(request, id=0):
    msg =""

    if request.method =='POST':
        form = forms.BrgyPurok(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Purok added successfully')
            return redirect('brgy_purok')
        else:
            messages.error(request, 'Purok already exist in the database')


    form = forms.BrgyPurok()
    context = {'segment': {'brgy_info', 'purok', 'add'}, 'form': form, 'msg': msg}
    html_template = loader.get_template('home/purok/purok_add.html')
    return HttpResponse(html_template.render(context, request))

def brgy_purok_edit(request, id=0):
    msg = ''

    if request.method =='POST':
        purok = models.purok.objects.get(pk=id)
        form = forms.BrgyPurok(request.POST, instance=purok)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Purok updated successfully')
            return redirect('brgy_purok')
        else:
            messages.error(request, 'Purok name is already in the database')

    purok = models.purok.objects.get(pk=id)
    form = forms.BrgyPurok(instance=purok)
    context = {'segment': {'brgy_info', 'purok', 'update'}, 'form': form, 'msg': msg}
    html_template = loader.get_template('home/purok/purok_add.html')
    return HttpResponse(html_template.render(context, request))


def brgy_purok_delete(request, id=0):
    purok = models.purok.objects.get(pk=id)
    if request.method == 'POST':
        purok.delete()
        messages.success(request, 'Purok deleted successfully')
        return redirect('brgy_purok')
    context = {'segment': {'brgy_info', 'purok'}, 'purok': purok}
    html_template = loader.get_template('home/purok/purok_delete.html')
    return HttpResponse(html_template.render(context, request))

def brgy_purok_import(request):
    if request.method == 'POST':
        purok_resource = PurokResource()
        dataset = Dataset()
        new_purok = request.FILES['file_import']

        imported_data = dataset.load(new_purok.read())
        result = purok_resource.import_data(dataset, dry_run=True)  # Test the data import
        if not result.has_errors():
            messages.success(request, 'Purok imported successfully')
            purok_resource.import_data(dataset, dry_run=False)
            return redirect('brgy_purok')
        else:
            messages.error(request, 'Error importing Purok')

    context = {'segment': {'brgy_info', 'purok'}, 'purok': purok}
    html_template = loader.get_template('home/purok/import_purok.html')
    return HttpResponse(html_template.render(context, request))


# RESIDENTS
def residents_list(request):
    _data = models.Resident.objects.all()
    print(_data)
    context = {'segment': 'residents', 'data': _data}
    html_template = loader.get_template('home/residents/residents_list.html')
    return HttpResponse(html_template.render(context, request))

def resident_delete(request, id=0):
    resident = models.Resident.objects.get(pk=id)
    if request.method == 'POST':
        resident.delete()
        messages.success(request, 'Resident deleted successfully')
        return redirect('residents_list')
    context = {'segment': {'residents', 'list'}, 'resident': resident}
    html_template = loader.get_template('home/residents/resident_delete.html')
    return HttpResponse(html_template.render(context, request))

def resident_add(request):
    if request.method == 'POST':
        form = forms.ResidentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Resident added successfully')
            return redirect('residents_list')
        else:
            messages.error(request, 'Error adding resident')

    form = forms.ResidentForm()
    context = {'segment': {'residents', 'add'}, 'form': form}
    html_template = loader.get_template('home/residents/residents_add.html')
    return HttpResponse(html_template.render(context, request))