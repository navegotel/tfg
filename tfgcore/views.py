from django.shortcuts import render

def landing(request):
    return render(request, 'tfgcore/landing.html')

def about(request):
    return render(request, 'tfgcore/sobre_la_encuesta.html')

def personaldata(request):
    return render(request, 'tfgcore/sobre_la_encuesta.html')