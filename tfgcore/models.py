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

    AGE_RANGE_CHOICES=[
        (1, '18-24'),
        (2, '25-34'),
        (3, '35-44'),
        (4, '45-54'),
        (5, '55-64'),
        (6, '65 y más')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Usuario con login")
    creation_date = models.DateTimeField("Creado", help_text="Fecha de creación del registro.", auto_now_add=True)
    age_range = models.IntegerField("Rango de edad", choices=AGE_RANGE_CHOICES, blank=True, null=True)
    gender = models.CharField("Género", max_length=12, choices=GENDER_CHOICES, blank=True, null=True)
    health_care_professional = models.BooleanField("Profesional sanitario", default=False)
    smoking = models.BooleanField("Fumador", default=False)
    sports = models.BooleanField("Deporte", blank=True, null=True)
    chronic_disease = models.BooleanField("Enf. crónica", default=False)   


class Answers(models.Model):
    FIVE_ITEMS_CHOICES=[
        (1, 'Sí'),
        (2, 'Creo que sí pero no estoy seguro'),
        (3, 'Creo que no pero no estoy seguro'),
        (4, 'No'),
        (5, 'Ni idea')
    ]
    CHOICES_ANSWER1=[
        (1, 'No'),
        (2, 'Sí, hace menos de un año'),
        (3, 'Sí, hace más de un año, pero menos de tres años'),
        (4, 'Sí, hace más de tres años')
    ]
    CHOICES_ANSWER6=[
        (1, "Entre 5 y 10 minutos"),
        (2, "Entre 10 15 minutos"),
        (3, "Entre 15 minutos y media hora"),
        (4, "Más de media hora"),
        (5, "El tiempo que sea necesario para que el cliente lo tenga claro, aunque sea más de una hora")
    ]

    CHOICES_LIKERT=[
        (1, "Estoy totalmente en desacuerdo"),
        (2, "Estoy un poco en desacuerdo"),
        (3, "Ni fu ni fa"),
        (4, "Estoy un poco de acuerdo"),
        (5, "Estoy totalmente de acuerdo")
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ¿Ha estado en tratamiento de fisioterapia en los últimos años?
    answer01 = models.IntegerField("Tratamiento reciente", choices=CHOICES_ANSWER1, default=1)
    
    # ¿Qué terapias o tratamientos ha aplicado el fisioterapeuta?
    answer01a = models.BooleanField("No me acuerdo", default=False)
    answer01b = models.BooleanField("Corrientes eléctricas", default=False)
    answer01c = models.BooleanField("Agujas", default=False)
    answer01d = models.BooleanField("Terapia manual, masajes o movilizaciones", default=False)
    answer01e = models.BooleanField("Ejercicio terapéutico", default=False)
    answer01f = models.BooleanField("Ultrasonido", default=False)
    answer01g = models.BooleanField("Magnetoterapia", default=False)
    answer01h = models.TextField("Otros tratamientos", blank=True, null=True)
    
    # ¿Con cuál de los siguientes problemas de salud acudiría a un fisioterapeuta?
    answer02a = models.IntegerField("Problemas respiratorios", blank=True, null=True)
    answer02b = models.IntegerField("Dolor de espalda", blank=True, null=True)
    answer02c = models.IntegerField("Dolor de hombro", blank=True, null=True)
    answer02d = models.IntegerField("Enfermedades relacionadas con el corazón", blank=True, null=True)
    answer02e = models.IntegerField("Dolor en las articulaciones", blank=True, null=True)
    answer02f = models.IntegerField("Diabetes", blank=True, null=True)
    answer02g = models.IntegerField("Parkinson", blank=True, null=True)
    answer02h = models.IntegerField("Problemas de visión o auditivos", blank=True, null=True)
    answer02i = models.IntegerField("Dolor de cabeza", blank=True, null=True)
    answer02j = models.IntegerField("Preparación al parto", blank=True, null=True)
    answer02k = models.IntegerField("Estreñimiento crónico", blank=True, null=True)

    # ¿Qué importancia tienen los siguientes factores para usted para elegir un fisioterapeuta?
    answer03a = models.IntegerField("Recomendación por parte de familiares o amigos", blank=True, null=True)
    answer03b = models.IntegerField("Recomendación por parte del médico", blank=True, null=True)
    answer03c = models.IntegerField("Fácil de llegar, distancia y aparcamiento", blank=True, null=True)
    answer03d = models.IntegerField("Especialización en el problema de salud que le afecte", blank=True, null=True)
    answer03e = models.IntegerField("Equipación con aparatos", blank=True, null=True)
    answer03f = models.IntegerField("Aplicación de determinadas técnicas (masaje, punción seca)", blank=True, null=True)
    
    # ¿Cuáles de las siguientes crees que son profesiones sanitarias reconocidas en España?
    answer04a = models.IntegerField("Osteopata", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    answer04b = models.IntegerField("Masajista", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    answer04c = models.IntegerField("Fisioterapeuta", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    answer04d = models.IntegerField("Podólogo", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    answer04e = models.IntegerField("Naturópata", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    answer04f = models.IntegerField("Quiropráctico", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    answer04g = models.IntegerField("Enfermero", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    answer04h = models.IntegerField("Farmacéutico", choices=FIVE_ITEMS_CHOICES, blank=True, null=True)
    
    # ¿Cuánta confianza tiene en las siguientes terapias?
    answer05a = models.IntegerField("Electroterapia", blank=True, null=True)
    answer05b = models.IntegerField("Punción seca (terapia con agujas)", blank=True, null=True)
    answer05c = models.IntegerField("Ejercicio terapéutico", blank=True, null=True)
    answer05c = models.IntegerField("Tratamiento con Láser", blank=True, null=True)
    answer05d = models.IntegerField("Bioresoncancia", blank=True, null=True)
    answer05e = models.IntegerField("Aplicación de frío o calor", blank=True, null=True)
    answer05f = models.IntegerField("Terapia manual y masaje", blank=True, null=True)
    answer05g = models.IntegerField("Aromaterapia", blank=True, null=True)
    answer05j = models.IntegerField("Magnetoterapia", blank=True, null=True)
    answer05k = models.IntegerField("Biodescodificación", blank=True, null=True)

    # ¿Qué importancia cree que tienen los ejercicios que el fisioterapeuta le pauta para hacerlos en casa?
    answer05 = models.IntegerField("Importancia ejercicio pautado", blank=True, null=True)

    # ¿Cree que el terapeuta debe dedicarle tiempo a darle información y explicaciones a su paciente?
    # ¿Cuánte tiempo le parecería adecuado?
    answer06 = models.IntegerField("Tiempo de educación", choices=CHOICES_ANSWER6, blank=True, null=True)

    # Qué importancia tienen para tí las siguientes características del fisioterapeuta
    answer05 = models.IntegerField("Sí es hombre o mujer", blank=True, null=True)
    #sexo, edad, nacionalidad

    # ¿Qué opina de las siguientes afirmaciones?
    answer08a = models.IntegerField("Una sesión de fisioterapia sin un masaje no está completo.", choices=CHOICES_LIKERT, blank=True, null=True)
    answer08b = models.IntegerField("Es inevitable que una sesión de fisioterapia sea algo dolorosa", choices=CHOICES_LIKERT, blank=True, null=True)
    answer08c = models.IntegerField("Cuanto más duele, mejor funciona", choices=CHOICES_LIKERT, blank=True, null=True)
    answer08d = models.IntegerField("Confío más en el fisioterapeuta que en el médico", choices=CHOICES_LIKERT, blank=True, null=True)
    answer08e = models.IntegerField("En la consulta de un fisioterapeuta tiene que haber un ecógrafo", choices=CHOICES_LIKERT, blank=True, null=True)
    answer08f = models.IntegerField("Un buen fisio también aplica terapias tradicionales aunque no tengan evidencia científica", choices=CHOICES_LIKERT, blank=True, null=True)

















