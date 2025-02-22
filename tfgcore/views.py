from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Participant

def landing(request):
    return render(request, 'tfgcore/landing.html')

def about(request):
    return render(request, 'tfgcore/sobre_la_encuesta.html')

def personaldata(request):
    if request.method == "POST":
        #TODO first check if the user is logged in
        try:
            h=hash(request.POST["email"])
            participants = Participant.objects.filter(hash=h)
            if len(participants) == 0:
                #TODO create user
                pass
        except KeyError:
            errmsg = "Tienes que especificar un correo electrónico válido."
        

        return redirect(reverse('tfgcore:question01'))
        
    return render(request, 'tfgcore/personaldata.html')


def question01(request):
    try:
        if request.POST["intreatment"] in ['2', '3']:
            return redirect(reverse('tfgcore:question02'))
        else: 
            return redirect(reverse('tfgcore:question03'))
    except KeyError:
        errmsq = "Tienes que marcar una de las opciones."
    return render(request, 'tfgcore/question01.html')


def question02(request):
    return render(request, 'tfgcore/question02.html')


def question03(request):
    return render(request, 'tfgcore/question03.html')


def legalstuff(request):
    return render(request, 'tfgcore/aviso_legal.html')


def testformwidgets(request):
    return render(request, 'tfgcore/testformwidgets.html')