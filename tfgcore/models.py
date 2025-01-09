from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):
    
    GENDER_CHOICES=[
        ('MALE', 'Hombre'),
        ('FEMALE', 'Mujer'),
        ('TRANSGENDER', 'Transgénero'),
        ('AGENDER', 'Asexual'),
        ('GENDERFLUID', 'Género fluido'),
        ('NONBINARY', 'Nonbinary'),
        ('GENDERQUEER', 'Género Queer'),
        ('NA', 'No quiero especificar'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Usuario con login")
    creation_date = models.DateTimeField("Creado", help_text="Fecha de creación del registro.", auto_now_add=True)
    date_of_birth = models.DateField("Fecha de nacimiento")
    gender = models.CharField("Género", max_length=12, choices=GENDER_CHOICES)
    post_code = models.CharField("Código Postal", max_length=5)
    smoking = models.BooleanField("Fumador")
    sports = models.IntegerField("Deportista")
    diabetes = models.BooleanField("Diabetes")
    ms = models.BooleanField("Esclerosis múltiple")
    parkinson = models.BooleanField("Morbus Parkinson")
    acv = models.BooleanField("Accidente cerebrovascular")
    hta = models.BooleanField("Hipertensión arterial")


class Question(models.Model):
    order = models.SmallIntegerField("Orden")
    question = models.TextField("Pregunta")
    justification = models.TextField("Justificación")


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField("Opción")


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vas = models.SmallIntegerField("EVA")
    comment = models.TextField("Comentario")
    yes = models.BooleanField("Sí")


class MultipleChoiceAnswers(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    vas = models.SmallIntegerField("EVA")
    yes = models.BooleanField("Sí")