from django.contrib import admin

from .models import WeekMenu, Restaurant

class WeekMenuAdmin(admin.ModelAdmin):
    save_as = True

# Register your models here.
admin.site.register(WeekMenu,WeekMenuAdmin)
admin.site.register(Restaurant)
