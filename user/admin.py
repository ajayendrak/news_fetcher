from django.contrib import admin
from user.models import *

class UserAdmin(admin.ModelAdmin):
    fields = ['email','first_name','last_name','phone_number', 'surf_limit']
    list_display = ['id','email','first_name','last_name','phone_number','is_staff','is_admin', 'surf_limit']
    search_fields = ['email','first_name','last_name']
admin.site.register(User,UserAdmin)