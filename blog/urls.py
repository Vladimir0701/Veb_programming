from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    # path('', Home.as_view(), name = 'home'),
    path('admin/', admin.site.urls),
    path('category/<slug:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<slug:slug>', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('text/', text, name = 'text'),
    path('list/', list, name = 'list'),
    path('table/', web_4, name = 'table'),
    path('cascad/', web_7, name = 'cascad'),
    path('web_8/', web_8, name = 'web_8'),
    path('web_91/', web_91, name = '1 задание 9 практикума'),
    path('web_92/', web_92, name = '2 задание 9 практикума'),
    path('web_93/', web_93, name = '3 задание 9 практикума'),
    path('web_94/', web_94, name = '4 задание 9 практикума'),
    path('posts/add-news', add_news, name='add_news'),
    path('', signup, name='signup'),
    path('crispy/', crispy_signup, name='crispy_signup'),
]


