
from django.shortcuts import render, redirect
from .forms import ProfesorForm, CursoForm, EstudianteForm

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_profesor')  # Redirige después de guardar
    else:
        form = ProfesorForm()

    return render(request, 'mi_app/form_profesor.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_curso')  # Redirige después de guardar
    else:
        form = CursoForm()

    return render(request, 'mi_app/form_curso.html', {'form': form})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_estudiante')  # Redirige después de guardar
    else:
        form = EstudianteForm()

    return render(request, 'mi_app/form_estudiante.html', {'form': form})

from django import forms
from models import Profesor, Curso, Estudiante

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'profesor']  

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'curso'] 

from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"       
    
