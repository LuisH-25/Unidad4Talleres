from django import forms

class InputForm(forms.Form):
    aula = forms.CharField(max_length=3)    # si se quita el required, es true por defecto
    hora_entrada = forms.TimeField(
        help_text='Ingrese la hora en formato HH:MM',
        label='Hora de la Entrada'
    )
    # TODO: Define form fields here
