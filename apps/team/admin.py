from django.contrib import admin
from .models import *


'''@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(TypeStudy)
class TypeStudyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)'''


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "secondname", "firstname", "faculty")
    list_display_links = ("secondname",)


'''@admin.register(Where)
class WhereAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    list_display_links = ("text",)'''


@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


admin.site.site_title = "Панель администратора"
admin.site.site_header = "Панель администратора"
