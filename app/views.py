from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import pytz
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    current_time_msk = current_time.astimezone(pytz.timezone('Europe/Moscow'))
    msg = f'Текущее время: {current_time_msk.strftime("%Y-%m-%d %H:%M:%S")}'
    return HttpResponse(msg)


def workdir_view(request):
    a = os.listdir('/home/gooder08/Projects/django/homework/dj-homeworks/first-project/first_project')
    dir = ''
    for file in a:
        dir += f'{file}, '
    return HttpResponse(dir)
