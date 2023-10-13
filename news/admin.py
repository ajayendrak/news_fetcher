from django.contrib import admin
from .models import *

class UserKeywordsAdmin(admin.ModelAdmin):
    fields = ['user','keyword']
    list_display = ['user','keyword','created_at']
    search_fields = ['keyword',]
admin.site.register(UserKeywords,UserKeywordsAdmin)