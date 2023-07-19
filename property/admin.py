from django.contrib import admin
from .models import Flat, Сomplaint, Owner


class MembershipInline(admin.TabularInline):
    model = Owner.flat.through


class FlatSettings(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', ]
    readonly_fields = ["created_at"]
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', ]
    list_editable = ['new_building',]
    list_filter = ['new_building', 'price']


class СomplaintSettings(admin.ModelAdmin):
    raw_id_fields = ['complaint']

class OwnerFlatSettings(admin.ModelAdmin):
    raw_id_fields = ['flat']
    inlines = [
        MembershipInline,
    ]
    exclude = ["flat"]



admin.site.register(Flat, FlatSettings)
admin.site.register(Сomplaint, СomplaintSettings)
admin.site.register(Owner, OwnerFlatSettings)
