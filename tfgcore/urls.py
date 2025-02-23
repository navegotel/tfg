from django.urls import path
from . import views

app_name = 'tfgcore'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about', views.about, name='about'),
    path('personaldata', views.personaldata, name='personaldata'),
    path('question01', views.question01, name='question01'),
    path('question02', views.question02, name='question02'),
    path('question03', views.question03, name='question03'),
    path('question04', views.question04, name='question04'),
    path('question05', views.question05, name='question05'),
    path('question06', views.question06, name='question06'),
    path('legalstuff', views.legalstuff, name='legalstuff'),
    path('testformwidgets', views.testformwidgets, name='testformwidgets'),
]
