from django.contrib import admin
from .models import Vase

class VaseAdmin(admin.ModelAdmin):
    list_display = ('vaseRef', 'collectionName', 'previousColl', 'provenanceName', 'height', 'diameter', 'publications', 'subject', 'fabric', 'technique', 'shapeName')

# Register your models here.

admin.site.register(Vase, VaseAdmin)