from django.contrib import admin
from .models import *
from django import forms


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)
    