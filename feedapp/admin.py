from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'user')
    search_fields = ('name', 'breed')
    list_filter = ('age', 'breed', 'user')
