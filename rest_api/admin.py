from django.contrib import admin
from .models import SnailsActivity, SnailsInventory, Pen, EggsInventory

# Register your models here.

# admin.site.register(SnailsActivity)
admin.site.register(SnailsInventory)
admin.site.register(Pen)
admin.site.register(EggsInventory)


@admin.register(SnailsActivity)
class SnailsActivityAdmin(admin.ModelAdmin):
    # list_display = '__all__'
    list_filter = ('dateTimeRecorded', 'specieType', 'penNumber',)
    search_fields = ('comments', 'penNumber',)
    date_hierarchy = 'dateTimeRecorded'
    ordering = ('-dateTimeRecorded', 'penNumber',)
