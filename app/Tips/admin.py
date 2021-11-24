from django.contrib import admin
from .models import TipModel


class TipModelAdmin(admin.ModelAdmin):
    list_display = ['date', 'tip']


# Register your models here.
admin.site.register(TipModel, TipModelAdmin)
