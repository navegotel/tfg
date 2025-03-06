import hashlib
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.datastructures import MultiValueDictKeyError
from django.urls import reverse
from .models import Participant, Answers

def landing(request):
    return render(request, 'tfgcore/landing.html')


def about(request):
    return render(request, 'tfgcore/sobre_la_encuesta.html')


def personaldata(request):
    def validate(p):
        msgs = []
        try:
            if len(p["email"]) == 0:
                msgs.append("Tienes que especificar un correo electrónico.")
            else:
                try:
                    validate_email(p["email"])
                except ValidationError:
                    msgs.append("El correo electrónico no parece ser válido.")
        except KeyError:
            msgs.append("Tienes que especificar un correo electrónico.")
        if int(p["agerange"]) == 0:
            print("works")
            msgs.append("Tienes que especificar un rango de edad.")
        if p["gender"] == "":
            msgs.append("Tienes que especificar tu género.")
        return msgs

    if request.method == "POST":
        msgs = validate(request.POST)
        m = hashlib.sha256()
        m.update(request.POST["email"].encode())
        username = m.hexdigest()
        if User.objects.filter(username = username).exists():
            msgs.append('parece que ya has participado en la encuesta. Solo se puede participar una vez.')
        if len(msgs)>0:
            return render(request, 'tfgcore/personaldata.html', {"msgs":msgs})
        email = "{0}@markusbarth.net".format(username)
        password = "unsecureP@sswrd"
        User.objects.create_user(username, email, password)
        usr = authenticate(username=username, password=password)
        login(request, usr)
        agerange = int(request.POST["agerange"])
        gender = request.POST["gender"]
        health_care_professional = False
        if request.POST["healthprofessional"] == "Yes":
            health_care_professional = True
        smoking = False
        if request.POST["smoker"] == "Yes":
            smoking = True
        sports = False
        if request.POST["sport"] == "Yes":
            sports = True
        chronic_disease = False
        if request.POST["pathologies"] == "Yes":
            chronic_disease = True
        

        participant = Participant(
            user=usr, 
            age_range=agerange, 
            gender=gender, 
            health_care_professional=health_care_professional,
            smoking=smoking,
            sports=sports,
            chronic_disease=chronic_disease
            )
        participant.save()
        
        return redirect(reverse('tfgcore:question01'))
    return render(request, 'tfgcore/personaldata.html')


@login_required
def question01(request):
    if request.method == "POST":
        msgs = []
        try:
            intreatment = request.POST["intreatment"]
        except MultiValueDictKeyError:
            msgs.append("Por favor, marca una de las respuestas.")
            return render(request, 'tfgcore/question01.html', {"msgs": msgs})
        answers = Answers(user=request.user, answer01=int(intreatment))
        answers.save()
        if intreatment in ['2', '3']:
            return redirect(reverse('tfgcore:question02'))
        else: 
            return redirect(reverse('tfgcore:question03'))
    return render(request, 'tfgcore/question01.html')


def question02(request):
    if request.method == "POST":
        msgs = []
        if request.POST.get('treatmenttype') is None and len(request.POST['othertreatment'])==0:
            msgs.append("Por favor, marca al menos una de las casillas o describe el tipo del tratamiento recibido en el cuadro de texto de abajo.")
            return render(request, 'tfgcore/question02.html', {"msgs":msgs})
        answers = Answers.objects.filter(user=request.user)[0]
        treatmenttype = request.POST.getlist('treatmenttype')
        if '1' in treatmenttype:
            answers.answer01a = True
        if '2' in treatmenttype:
            answers.answer01b = True
        if '3' in treatmenttype:
            answers.answer01c = True
        if '4' in treatmenttype:
            answers.answer01d = True
        if '5' in treatmenttype:
            answers.answer01e = True
        if '6' in treatmenttype:
            answers.answer01f = True
        if '7' in treatmenttype:
            answers.answer01g = True
        if len(request.POST['othertreatment'])>0:
            answers.answer01h = request.POST['othertreatment']
        answers.save()
        return redirect(reverse('tfgcore:question03'))
    return render(request, 'tfgcore/question02.html')


def question03(request):
    if request.method == "POST":
        msgs = []
        if request.POST.get('relatedtreatments') is None:
            msgs.append("Por favor, marca al menos una de las casillas.")
            return render(request, 'tfgcore/question03.html', {"msgs": msgs})
        answers = Answers.objects.filter(user=request.user)[0]
        relatedtreatments = request.POST.getlist('relatedtreatments')
        if '1' in relatedtreatments:
            answers.answer02a = True
        if '2' in relatedtreatments:
            answers.answer02b = True
        if '3' in relatedtreatments:
            answers.answer02c = True
        if '4' in relatedtreatments:
            answers.answer02d = True
        if '5' in relatedtreatments:
            answers.answer02e = True
        if '6' in relatedtreatments:
            answers.answer02f = True
        if '7' in relatedtreatments:
            answers.answer02g = True
        if '8' in relatedtreatments:
            answers.answer02h = True
        if '9' in relatedtreatments:
            answers.answer02i = True
        if '10' in relatedtreatments:
            answers.answer02j = True
        if '11' in relatedtreatments:
            answers.answer02k = True
        answers.save()
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