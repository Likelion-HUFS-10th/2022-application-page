from django.contrib import admin
from .models import User

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    """"Admin View for User"""
    
    list_display = (
        "name",
        "email",
        "phone_num",
    )

