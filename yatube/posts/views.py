from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Главная страница Yatube</h1>')


def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')

#для страницы, на которой будут посты, отфильтрованные по группам.
def group_posts(request,gp):
    return HttpResponse('Информация для страницы, на которой будут посты, отфильтрованные по группам.<br>\n'
                        + f'Номер поста {gp}')
