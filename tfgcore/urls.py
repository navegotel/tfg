from django.urls import path
from . import views

app_name = 'tfgcore'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about', views.about, name='about'),
    path('personaldata', views.personaldata, name='personaldata'),
]