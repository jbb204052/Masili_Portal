from import_export import resources
from .models import purok

class PurokResource(resources.ModelResource):
    class Meta:
        model = purok
        import_id_fields = ('purok_name',)
        exclude = ('id',)