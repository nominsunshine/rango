from django.contrib import admin
from rango.models import Category, Page


# This makes slug auto-fill from name
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register models with admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)