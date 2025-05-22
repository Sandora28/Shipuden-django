from django.contrib import admin

# Register your models here.
from . models import Ninja,Mission,Jutsu,Team

class NinjaAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'village')  # Fields you want to show in the list
    search_fields = ('name', 'village')         # Optional search bar

class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank', 'status')
    list_filter = ('rank', 'status')
    search_fields = ('title',)
admin.site.register(Ninja)
admin.site.register(Mission)
admin.site.register(Jutsu)
admin.site.register(Team)
