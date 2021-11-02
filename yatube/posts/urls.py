# posts/urls.py
from django.urls import path

from . import views

# Эта строчка обязательна.
# Без нее чуда не произойдет и namespace работать не будет
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('ice_cream/',views.ice_cream_list, name='icecream_list'),
    path(
        'ice_cream/<int:pk>/',
        views.ice_cream_detail,
        name='icecream_detail'
    ),
    path('group/<int:gp>',views.group_posts, name='group_posts'),

] 