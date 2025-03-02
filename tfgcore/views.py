from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from .models import Participant

def landing(request):
    return render(request, 'tfgcore/landing.html')


def about(request):
    return render(request, 'tfgcore/sobre_la_encuesta.html')


def personaldata(request):
    if request.method == "POST":
        msgs = []
        try:
            if len(request.POST["email"]) == 0:
                msgs.append("Tienes que especificar un correo electrónico.")
            else:
                try:
                    validate_email(request.POST["email"])
                except ValidationError:
                    msgs.append("El correo electrónico no parece ser válido.")
        except KeyError:
            msgs.append("Tienes que especificar un correo electrónico.")
        if len(msgs)>0:
            return render(request, 'tfgcore/personaldata.html', {"msgs":msgs})
        h=hash(request.POST["email"])
        participants = Participant.objects.filter(hash=h)
        if len(participants) == 0:
            username = str(abs(h))
            email = "{0}@markusbarth.net".format(username)
            password = "unsecureP@sswrd"
            User.objects.create_user(username, email, password)
            usr = authenticate(username=username, password=password)
            
        return redirect(reverse('tfgcore:question01'))
        
    return render(request, 'tfgcore/personaldata.html')

@login_required
def question01(request):
    try:
        if request.POST["intreatment"] in ['2', '3']:
            return redirect(reverse('tfgcore:question02'))
        else: 
            return redirect(reverse('tfgcore:question03'))
    except KeyError:
        msq = "Tienes que marcar una de las opciones."
    return render(request, 'tfgcore/question01.html')


def question02(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:question03'))
    return render(request, 'tfgcore/question02.html')


def question03(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:question04'))
    return render(request, 'tfgcore/question03.html')


def question04(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:question05'))
    return render(request, 'tfgcore/question04.html')


def question05(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:question06'))
    return render(request, 'tfgcore/question05.html')


def question06(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:question07'))
    return render(request, 'tfgcore/question06.html')


def question07(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:question08'))
    return render(request, 'tfgcore/question07.html')


def question08(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:question09'))
    return render(request, 'tfgcore/question08.html')


def question09(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:bye.html'))
    return render(request, 'tfgcore/question09.html')


def bye(request):
    if request.method == "POST":
        return redirect(reverse('tfgcore:bye'))
    return render(request, 'tfgcore/bye.html')

def legalstuff(request):
    return render(request, 'tfgcore/aviso_legal.html')


def testformwidgets(request):
    return render(request, 'tfgcore/testformwidgets.html')