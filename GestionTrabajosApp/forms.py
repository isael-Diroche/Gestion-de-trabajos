from django.forms import *

class NuevoTrabajo(Form):
    OPCIONES = (('', 'Seleccionar'), ('normal', 'Dia normal'), ('extra', 'Dia extra'), ('limon', 'Dia de limones'), ('targeta', 'Dia de targeta'))
    type = ChoiceField(label='Tipo de trabajo', choices=OPCIONES, required=True)
    comment = CharField(label='Comentario', max_length=500, required=False)



