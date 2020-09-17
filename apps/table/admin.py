from django.contrib import admin
from .models import *


@admin.register(Concurse)
class ConcurseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Ball)
class BallAdmin(admin.ModelAdmin):
    list_display = ("id", "conc", "team", "ball", "time")
    list_display_links = ("conc",)
