from django.contrib import admin
from .models import New

class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'add_date', 'shop')

# Register your models here.
admin.site.register(New,NewAdmin)