from django.conf import settings
from apps.home import models

def cfg_assets_root(request):

    return { 'ASSETS_ROOT' : settings.ASSETS_ROOT }

def logo_url(request):
    _data = models.brgy_info.objects.first()
    if _data:
        return {'logo_url': _data.logo.url}
    else:
        return {'logo_url': None}