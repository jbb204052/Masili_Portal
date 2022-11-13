# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    path('info/', views.brgy_info, name='brgy_info'),
    path('purok/', views.brgy_purok, name='brgy_purok'),
    path('purok/add/', views.brgy_purok_add, name='brgy_purok_add'),
    path('purok/edit/<int:id>', views.brgy_purok_edit, name='brgy_purok_edit'),
    path('purok/delete/<int:id>', views.brgy_purok_delete, name='brgy_purok_delete'),
    path('purok/import/', views.brgy_purok_import, name='brgy_purok_import'),

    # Residents
    path('residents/', views.residents_list, name='brgy_residents'),
    path('residents/add/', views.resident_add, name='brgy_resident_add'),
    path('residents/edit/<int:id>', views.resident_edit, name='brgy_residents_edit'),
    path('residents/delete/<int:id>', views.resident_delete, name='brgy_residents_delete'),
    path('resident/views/<int:id>', views.resident_view, name='resident_view'),
]
