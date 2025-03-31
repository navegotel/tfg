import hashlib
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
            msgs.append("Tienes que especificar un rango de edad.")
        if p["gender"] == "":
            msgs.append("Tienes que especificar tu género.")
        return msgs
    
    def populate(p):
        formdata = {
            "agerange": p.get('agerange'),
            "gender": p.get('gender'),
            "email": p.get('email'),
            "education": p.get('education')
        }
        return formdata

    if request.method == "POST":
        msgs = validate(request.POST)
        m = hashlib.sha256()
        m.update(request.POST["email"].encode())
        username = m.hexdigest()
        if User.objects.filter(username = username).exists():
            msgs.append('parece que ya has participado en la encuesta. Solo se puede participar una vez.')
        if len(msgs)>0:
            formdata = populate(request.POST)
            return render(request, 'tfgcore/personaldata.html', {"msgs":msgs, "formdata": formdata})
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


@login_required
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
        if '8' in treatmenttype:
            answers.answer01h = True
        if len(request.POST['othertreatment'])>0:
            answers.answer01i = request.POST['othertreatment']
        answers.save()

        return redirect(reverse('tfgcore:question03'))
    return render(request, 'tfgcore/question02.html')


@login_required
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


@login_required
def question04(request):
    if request.method == "POST":
        answers = Answers.objects.filter(user=request.user)[0]
        answers.answer03a = int(request.POST.get('answer03a'))
        answers.answer03b = int(request.POST.get('answer03b'))
        answers.answer03c = int(request.POST.get('answer03c'))
        answers.answer03d = int(request.POST.get('answer03d'))
        answers.answer03e = int(request.POST.get('answer03e'))
        answers.answer03f = int(request.POST.get('answer03f'))
        answers.answer03g = int(request.POST.get('answer03g'))
        answers.answer03other = (request.POST.get('otherreasons'))
        answers.save()
        return redirect(reverse('tfgcore:question05'))
    return render(request, 'tfgcore/question04.html')


@login_required
def question05(request):
    if request.method == "POST":
        msgs = []
        if request.POST.get('healthprofession') is None:
            msgs.append("No has marcado ninguna de las opciones.")
            return render(request, 'tfgcore/question05.html', {'msgs': msgs})
        answers = Answers.objects.filter(user=request.user)[0]
        healthprofession = request.POST.getlist('healthprofession')
        if '1' in healthprofession:
            answers.answer04a = True
        if '2' in healthprofession:
            answers.answer04b = True
        if '3' in healthprofession:
            answers.answer04c = True
        if '4' in healthprofession:
            answers.answer04d = True
        if '5' in healthprofession:
            answers.answer04e = True
        if '6' in healthprofession:
            answers.answer04f = True
        if '7' in healthprofession:
            answers.answer04g = True
        if '8' in healthprofession:
            answers.answer04h = True
        answers.save()
        return redirect(reverse('tfgcore:question06'))
    return render(request, 'tfgcore/question05.html')


@login_required
def question06(request):
    if request.method == "POST":
        if 'knowntreatments' in request.POST:
            knowntreatments = request.POST.getlist('treatment')
            if len(knowntreatments) == 0:
                # user doesn't know any treatments so he cannot review any treatments -> we send him to the next view in the questionnaire.
                return redirect(reverse('tfgcore:question07'))
            else:
                print(knowntreatments)
                return render(request, 'tfgcore/question06b.html', {'knowntreatments': knowntreatments})
        else:
            print(request.POST)
            answers = Answers.objects.filter(user=request.user)[0]
            answers.answer05a = int(request.POST.get('answer05a', -1))
            answers.answer05b = int(request.POST.get('answer05b', -1))
            answers.answer05c = int(request.POST.get('answer05c', -1))
            answers.answer05d = int(request.POST.get('answer05d', -1))
            answers.answer05e = int(request.POST.get('answer05e', -1))
            answers.answer05f = int(request.POST.get('answer05f', -1))
            answers.answer05g = int(request.POST.get('answer05g', -1))
            answers.answer05h = int(request.POST.get('answer05h', -1))
            answers.answer05i = int(request.POST.get('answer05i', -1))
            answers.answer05j = int(request.POST.get('answer05j', -1))
            answers.answer05other = request.POST.get('others')
            answers.save()
            return redirect(reverse('tfgcore:question07'))
    return render(request, 'tfgcore/question06a.html')


@login_required
def question07(request):
    if request.method == "POST":
        answers = Answers.objects.filter(user=request.user)[0]
        answers.answer06 = int(request.POST.get('answer06'))
        answers.save()
        return redirect(reverse('tfgcore:question08'))
    return render(request, 'tfgcore/question07.html')


def question08(request):
    if request.method == "POST":
        msgs = []
        try:
            answer07 = request.POST["answer07"]
        except MultiValueDictKeyError:
            msgs.append("Por favor, marca una de las respuestas.")
            return render(request, 'tfgcore/question08.html', {"msgs": msgs})
        answers = Answers.objects.filter(user=request.user)[0]
        answers.answer07 = int(answer07)
        answers.save()
        return redirect(reverse('tfgcore:question09'))
    return render(request, 'tfgcore/question08.html')


def question09(request):
    if request.method == "POST":
        answers = Answers.objects.filter(user=request.user)[0]
        answers.answer08a = request.POST["answer08a"]
        answers.answer08b = request.POST["answer08b"]
        answers.answer08c = request.POST["answer08c"]
        answers.answer08d = request.POST["answer08d"]
        answers.answer08e = request.POST["answer08e"]
        answers.answer08f = request.POST["answer08f"]
        answers.save()
        logout(request)
        return redirect(reverse('tfgcore:bye'))
    return render(request, 'tfgcore/question09.html')


def bye(request):
    return render(request, 'tfgcore/bye.html')

def legalstuff(request):
    return render(request, 'tfgcore/aviso_legal.html')


def testformwidgets(request):
    return render(request, 'tfgcore/testformwidgets.html')