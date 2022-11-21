from django import forms
from django.forms import ModelForm
from django.core import validators
from django.core.validators import RegexValidator
from veterinariaApp.models import *

class mascotaForm(forms.Form):

    MOTIVO = [('consultas medica', 'CONSULTAS MEDICAS'), ('estética veterinaria', 'ESTÉTICA VETERINARIA'), ('vacunas', 'VACUNAS'), ('cirugías', 'CIRUGÍAS')]
    nombre = forms.CharField(validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')])
    fechaAtencion = forms.DateField(label="Fecha de Atención")
    motivo = forms.CharField(widget=forms.Select(choices=MOTIVO), required=True)
    diagnostico = forms.CharField(label="Diagnostico del paciente", max_length=100, required=True)
    observaciones = forms.CharField(label="Observaciones del doctor", max_length=100, required=True)
    valor = forms.IntegerField(label="Valor de la consulta")
    edad = forms.IntegerField(label="Edad de la mascota", required=True)
    descripcion = forms.CharField(label="Descripcion de la consulta", max_length=100)
    nombreDueño = forms.CharField(label= 'Nombre del dueño de la mascota', validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')])
    apellidoDueño = forms.CharField(label='Apellido del duño de la mascota',validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El apellido debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')])
    emailDueño=forms.EmailField(label="Email dueño de la mascota")
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre

    def clean_nombreDueño(self):
        nombreDueño = self.cleaned_data.get('nombreDueño')
        if len(nombreDueño) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombreDueño

    def clean_apellidoDueño(self):
        apellidoDueño = self.cleaned_data.get('apellidoDueño')
        if len(apellidoDueño) < 4:
            raise forms.ValidationError("El apellido debe tener al menos 4 caracteres")
        return apellidoDueño


class mascotaForm(ModelForm):
    class Meta:
        model = Mascotas
        fields = '__all__'
    
    MOTIVO = [('consultas medica', 'CONSULTAS MEDICAS'), ('estética veterinaria', 'ESTÉTICA VETERINARIA'), ('vacunas', 'VACUNAS'), ('cirugías', 'CIRUGÍAS')]
    nombre = forms.CharField(validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')])
    fechaAtencion = forms.DateField(label="Fecha de Atención")
    motivo = forms.CharField(widget=forms.Select(choices=MOTIVO), required=True)
    diagnostico = forms.CharField(label="Diagnostico del paciente", max_length=100, required=True)
    observaciones = forms.CharField(label="Observaciones del doctor", max_length=100, required=True)
    valor = forms.IntegerField(label="Valor de la consulta")
    edad = forms.IntegerField(label="Edad de la mascota", required=True)
    descripcion = forms.CharField(label="Descripcion de la consulta", max_length=100)
    nombreDueño = forms.CharField(label='Nombre del dueño de la mascota', validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El nombre debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')])
    apellidoDueño = forms.CharField(label='Apellido del duño de la mascota',validators=[
        RegexValidator(regex='^[A-Z][a-z]*$', message='El apellido debe comenzar con mayúscula y no debe contener números'),
        validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres'),
        validators.MaxLengthValidator(30, 'El nombre debe tener máximo 30 caracteres')])
    emailDueño=forms.EmailField(label="Email dueño de la mascota")
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombre

    def clean_nombreDueño(self):
        nombreDueño = self.cleaned_data.get('nombreDueño')
        if len(nombreDueño) < 4:
            raise forms.ValidationError("El nombre debe tener al menos 4 caracteres")
        return nombreDueño

    def clean_apellidoDueño(self):
        apellidoDueño = self.cleaned_data.get('apellidoDueño')
        if len(apellidoDueño) < 4:
            raise forms.ValidationError("El apellido debe tener al menos 4 caracteres")
        return apellidoDueño
