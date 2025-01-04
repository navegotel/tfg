from django.db import models

class Participant(models.Model):
    class Meta:
        ordering = ['last_name', 'first_name']

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

    email = models.EmailField("Correo electrónico")
    creation_date = models.DateTimeField("Creado", help_text="Fecha de creación del registro.", auto_now_add=True)
    last_name = models.CharField("Apellidos", max_length=50)
    first_name = models.CharField("Nombre", max_length=50)
    date_of_birth = models.DateField("Fecha de nacimiento")
    gender = models.CharField("Género", max_length=12, choices=GENDER_CHOICES)
    post_code = models.CharField("Código Postal", max_length=5)


class ClinicalProfile(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
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


class MultipleChoiceAnswers(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    vas = models.SmallIntegerField("EVA")