# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.


admin.site.register(models.brgy_info)

@admin.register(models.purok)
class PurokAdmin(ImportExportModelAdmin):
    exclude = ('id',)

class ResidentAdmin(admin.ModelAdmin):
    list_display = ('res_fname', 'res_lname', 'res_mname')
admin.site.register(models.Resident, ResidentAdmin)