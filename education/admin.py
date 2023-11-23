from django.contrib import admin
from education.models import Сourse, Lesson


# Register your models here.

@admin.register(Сourse)
class СourseAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('description', 'title',)


