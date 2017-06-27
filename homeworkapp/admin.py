from django.contrib import admin
from .models import Lesson, Homework

# Register your models here.
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'startdate', 'submit', 'deadline', 'valid', 'content')


admin.site.register(Lesson)
admin.site.register(Homework, HomeworkAdmin)
