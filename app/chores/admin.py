from django.contrib import admin
from .models import Task

@admin.register(Task)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at")
    list_filter = ("title",)
    search_fields = ("title",)