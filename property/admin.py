from django.contrib import admin
from .models import Flat


class SearchAddress(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', ]


admin.site.register(Flat, SearchAddress)
