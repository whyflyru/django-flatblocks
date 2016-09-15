from django.contrib import admin
from flatblocks.models import FlatBlock


class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['slug', ]
    list_display = ('slug', 'header', 'subdomain', 'content')
    search_fields = ('slug', 'header', 'content', 'subdomain')

admin.site.register(FlatBlock, FlatBlockAdmin)
