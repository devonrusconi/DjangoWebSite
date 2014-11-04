from django.contrib import admin

# Register your models here.
from devon.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)
