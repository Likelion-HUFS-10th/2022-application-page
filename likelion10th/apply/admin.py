from django.contrib import admin
from .models import Apply

@admin.register(Apply)
class Applyadmin(admin.ModelAdmin):
    """"Admin View for Apply"""
    
    list_display = (
        "user",
        "is_completed",
    )
    readonly_fields = (
        "user",
    )
