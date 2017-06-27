# -*- coding: utf-8 -*-
# from django.utils.translation import ugettext as _
from django.shortcuts import render

from .models import Homework, Lesson

# Create your views here.
def display(request):
    contents = []
    all_homework = Homework.objects.all().values(
        'name', 'startdate', 'submit', 'deadline', 'valid', 'content')
    all_lesson = Lesson.objects.all().values('id', 'lesson')
    dict_lesson = dict([tuple(x.values()) for x in list(all_lesson)])
    for item in all_homework:
        iname = item['name']
        item['name'] = dict_lesson.get(iname, iname)
        contents.append(item)

    return render(request, 'display.html', {'homework_list': contents})
