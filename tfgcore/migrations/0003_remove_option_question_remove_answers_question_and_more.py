# Generated by Django 5.1.3 on 2025-02-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfgcore', '0002_alter_participant_options_remove_participant_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='vas',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='yes',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='acv',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='hta',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='ms',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='parkinson',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='post_code',
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01',
            field=models.IntegerField(choices=[(1, 'No'), (2, 'Sí, hace menos de un año'), (3, 'Sí, hace más de un año, pero menos de tres años'), (4, 'Sí, hace más de tres años')], default=1, verbose_name='Tratamiento reciente'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01b',
            field=models.BooleanField(default=False, verbose_name='Corrientes eléctricas'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01c',
            field=models.BooleanField(default=False, verbose_name='Agujas'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01d',
            field=models.BooleanField(default=False, verbose_name='Movilizaciones y masaje'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01e',
            field=models.BooleanField(default=False, verbose_name='Ejercicio terapéutico'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01f',
            field=models.BooleanField(default=False, verbose_name='Ultrasonido'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01g',
            field=models.BooleanField(default=False, verbose_name='Magnetoterapia'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer01h',
            field=models.TextField(blank=True, null=True, verbose_name='Otros tratamientos'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02a',
            field=models.IntegerField(blank=True, null=True, verbose_name='Problemas respiratorios'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02b',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dolor de espalda'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02c',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dolor de hombro'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02d',
            field=models.IntegerField(blank=True, null=True, verbose_name='Enfermedades relacionadas con el corazón'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02e',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dolor en las articulaciones'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02f',
            field=models.IntegerField(blank=True, null=True, verbose_name='Diabetes'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02g',
            field=models.IntegerField(blank=True, null=True, verbose_name='Parkinson'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02h',
            field=models.IntegerField(blank=True, null=True, verbose_name='Problemas de visión o auditivos'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02i',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dolor de cabeza'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02j',
            field=models.IntegerField(blank=True, null=True, verbose_name='Preparación al parto'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer02k',
            field=models.IntegerField(blank=True, null=True, verbose_name='Estreñimiento crónico'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer03a',
            field=models.IntegerField(blank=True, null=True, verbose_name='Recomendación por parte de familiares o amigos'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer03b',
            field=models.IntegerField(blank=True, null=True, verbose_name='Recomendación por parte del médico'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer03c',
            field=models.IntegerField(blank=True, null=True, verbose_name='Distancia y aparacamiento'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer03d',
            field=models.IntegerField(blank=True, null=True, verbose_name='Especialización en el problema de salud que le afecte'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer03e',
            field=models.IntegerField(blank=True, null=True, verbose_name='Equipación con aparatos'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer03f',
            field=models.IntegerField(blank=True, null=True, verbose_name='Aplicación de determinadas técnicas (masaje, punción seca)'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer04a',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí'), (2, 'Creo que sí pero no estoy seguro'), (3, 'Creo que no pero no estoy seguro'), (4, 'No'), (5, 'Ni idea')], null=True, verbose_name='Osteopata'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer04b',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí'), (2, 'Creo que sí pero no estoy seguro'), (3, 'Creo que no pero no estoy seguro'), (4, 'No'), (5, 'Ni idea')], null=True, verbose_name='Masajista'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer04c',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí'), (2, 'Creo que sí pero no estoy seguro'), (3, 'Creo que no pero no estoy seguro'), (4, 'No'), (5, 'Ni idea')], null=True, verbose_name='Fisioterapeuta'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer04d',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí'), (2, 'Creo que sí pero no estoy seguro'), (3, 'Creo que no pero no estoy seguro'), (4, 'No'), (5, 'Ni idea')], null=True, verbose_name='Podólogo'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer04e',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí'), (2, 'Creo que sí pero no estoy seguro'), (3, 'Creo que no pero no estoy seguro'), (4, 'No'), (5, 'Ni idea')], null=True, verbose_name='Naturópata'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer04f',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí'), (2, 'Creo que sí pero no estoy seguro'), (3, 'Creo que no pero no estoy seguro'), (4, 'No'), (5, 'Ni idea')], null=True, verbose_name='Quiropráctico'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer04g',
            field=models.IntegerField(blank=True, choices=[(1, 'Sí'), (2, 'Creo que sí pero no estoy seguro'), (3, 'Creo que no pero no estoy seguro'), (4, 'No'), (5, 'Ni idea')], null=True, verbose_name='Enfermero'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sí es hombre o mujer'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05a',
            field=models.IntegerField(blank=True, null=True, verbose_name='Electroterapia'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05b',
            field=models.IntegerField(blank=True, null=True, verbose_name='Punción seca (terapia con agujas)'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05c',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tratamiento con Láser'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05d',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bioresoncancia'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05e',
            field=models.IntegerField(blank=True, null=True, verbose_name='Aplicación de frío o calor'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05f',
            field=models.IntegerField(blank=True, null=True, verbose_name='Terapia manual y masaje'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05g',
            field=models.IntegerField(blank=True, null=True, verbose_name='Aromaterapia'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05j',
            field=models.IntegerField(blank=True, null=True, verbose_name='Magnetoterapia'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer05k',
            field=models.IntegerField(blank=True, null=True, verbose_name='Biodescodificación'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer06',
            field=models.IntegerField(blank=True, choices=[(1, 'Entre 5 y 10 minutos'), (2, 'Entre 10 15 minutos'), (3, 'Entre 15 minutos y media hora'), (4, 'Más de media hora'), (5, 'El tiempo que sea necesario para que el cliente lo tenga claro, aunque sea más de una hora')], null=True, verbose_name='Tiempo de educación'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer08a',
            field=models.IntegerField(blank=True, choices=[(1, 'Estoy totalmente en desacuerdo'), (2, 'Estoy un poco en desacuerdo'), (3, 'Ni fu ni fa'), (4, 'Estoy un poco de acuerdo'), (5, 'Estoy totalmente de acuerdo')], null=True, verbose_name='Una sesión de fisioterapia sin un masaje no está completo.'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer08b',
            field=models.IntegerField(blank=True, choices=[(1, 'Estoy totalmente en desacuerdo'), (2, 'Estoy un poco en desacuerdo'), (3, 'Ni fu ni fa'), (4, 'Estoy un poco de acuerdo'), (5, 'Estoy totalmente de acuerdo')], null=True, verbose_name='Es inevitable que una sesión de fisioterapia sea algo dolorosa'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer08c',
            field=models.IntegerField(blank=True, choices=[(1, 'Estoy totalmente en desacuerdo'), (2, 'Estoy un poco en desacuerdo'), (3, 'Ni fu ni fa'), (4, 'Estoy un poco de acuerdo'), (5, 'Estoy totalmente de acuerdo')], null=True, verbose_name='Cuanto más duele, mejor funciona'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer08d',
            field=models.IntegerField(blank=True, choices=[(1, 'Estoy totalmente en desacuerdo'), (2, 'Estoy un poco en desacuerdo'), (3, 'Ni fu ni fa'), (4, 'Estoy un poco de acuerdo'), (5, 'Estoy totalmente de acuerdo')], null=True, verbose_name='Confío más en el fisioterapeuta que en el médico'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer08e',
            field=models.IntegerField(blank=True, choices=[(1, 'Estoy totalmente en desacuerdo'), (2, 'Estoy un poco en desacuerdo'), (3, 'Ni fu ni fa'), (4, 'Estoy un poco de acuerdo'), (5, 'Estoy totalmente de acuerdo')], null=True, verbose_name='En la consulta de un fisioterapeuta tiene que haber un ecógrafo'),
        ),
        migrations.AddField(
            model_name='answers',
            name='answer08f',
            field=models.IntegerField(blank=True, choices=[(1, 'Estoy totalmente en desacuerdo'), (2, 'Estoy un poco en desacuerdo'), (3, 'Ni fu ni fa'), (4, 'Estoy un poco de acuerdo'), (5, 'Estoy totalmente de acuerdo')], null=True, verbose_name='Un buen fisio también aplica terapias tradicionales aunque no tengan evidencia científica'),
        ),
        migrations.AddField(
            model_name='participant',
            name='age_range',
            field=models.IntegerField(blank=True, choices=[(1, '18-24'), (2, '25-34'), (3, '35-44'), (4, '45-54'), (5, '55-64'), (6, '65 y más')], null=True, verbose_name='Rango de edad'),
        ),
        migrations.AddField(
            model_name='participant',
            name='chronic_disease',
            field=models.BooleanField(default=False, verbose_name='Enf. crónica'),
        ),
        migrations.AddField(
            model_name='participant',
            name='health_care_professional',
            field=models.BooleanField(default=False, verbose_name='Profesional sanitario'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'Hombre'), ('FEMALE', 'Mujer'), ('TRANSGENDER', 'Transgénero'), ('AGENDER', 'Asexual'), ('GENDERFLUID', 'Género fluido'), ('NONBINARY', 'Nonbinary'), ('GENDERQUEER', 'Género Queer'), ('NA', 'No quiero especificar')], max_length=12, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='smoking',
            field=models.BooleanField(default=False, verbose_name='Fumador'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='sports',
            field=models.IntegerField(blank=True, null=True, verbose_name='Deporte'),
        ),
        migrations.DeleteModel(
            name='MultipleChoiceAnswers',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
