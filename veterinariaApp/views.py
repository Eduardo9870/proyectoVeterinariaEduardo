from django.shortcuts import render, redirect
from veterinariaApp.models import Mascotas
from veterinariaApp.forms import *
from django.db.models import Avg, Max, Min, Count
# Create your views here.


def index(request):
    return render(request, 'index.html')

def viewMascotas(request):
    mascotas = Mascotas.objects.all()
    promedio = Mascotas.objects.all().aggregate(Avg('valor'))
    max = Mascotas.objects.all().aggregate(Max('valor'))
    min = Mascotas.objects.all().aggregate(Min('valor'))
    count = Mascotas.objects.all().aggregate(Count('id'))
    data ={
        'mascotas': mascotas,
        'titulo': 'Mascotas',
        'promedio': promedio,
        'max' : max,
        'min' : min,
        'count' : count
    }
    return render(request, 'viewMascotas.html', data)

def addMascota(request):
    data ={
        'titulo' : 'Registro mascotas',
        'form' : mascotaForm()
    }
    if (request.method) == 'POST':
        formulario = mascotaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/mascotas')
        else:
            data['form'] = formulario
    return render(request, 'formMascotas.html', data)

def viewVacuna(request):
    mascota = Mascotas.objects.all().filter(motivo = 'Vacunas')
    data ={
        'mascota':mascota,
        'titulo': 'Vacunas'
    }
    return render(request, 'viewMotivos.html', data)

def viewConsultaMedica(request):
    mascota = Mascotas.objects.all().filter(motivo='CONSULTAS MEDICAS')
    data ={
        'mascota': mascota,
        'titulo': 'Consulta Medica'
        }
    return render(request, 'viewMotivos.html', data)

def viewEsteticaVeterinaria(request):

    mascota = Mascotas.objects.all().filter(motivo='ESTÉTICA VETERINARIA')
    data ={
       'mascota': mascota,
        'titulo' :'Estetica Verinaria'
    }
    return render(request, 'viewMotivos.html', data)

def viewCirugia(request):
    mascota = Mascotas.objects.all().filter(motivo='CIRUGÍAS')
    data = {
        'mascota': mascota,
        'titulo': 'Cirugia'
    }
    return render(request, 'viewMotivos.html', data)

def deleteMascota(request, id):
    mascota = Mascotas.objects.get(id=id)
    mascota.delete()
    return redirect('/mascotas')

def editarMascota(request, id):
    form = Mascotas.objects.get(id=id)
    data = {
        'titulo' : 'Editar mascota',
        'form' : mascotaForm(instance=form)
    }
    if (request.method == 'POST'):
        form = mascotaForm(request.POST, instance=form)
        if (form.is_valid()):
            form.save()
            return redirect('/mascotas')
        else:
            data['form'] = form
    return render(request, 'formMascotas.html', data)
    