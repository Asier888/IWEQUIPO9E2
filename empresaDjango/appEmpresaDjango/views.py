from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Empleado, Tarea, Proyecto
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Listado de departamentos")

# Mostrar la lista de empleados ordenados por id
def pruebalista(request):
    empleados = Empleado.objects.order_by('id')
    context = {
        'lista_empleado': empleados,
        'titulo_pagina': 'Listado de empleados',
        'titulo_pagina1': 'Empleados'
    }
    return render(request, 'lista_empleados.html', context)

# Mostrar un único empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del empleado'
        context['titulo_pagina1'] = 'Detalles del empleado'
        print(context)
        return context

# Creación de un nuevo empleado
def show_form(request):
    return render(request, 'crear_empleado.html')

def crearempleado(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dni = request.POST["dni"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]

    empleado = Empleado(
        nombre=nombre,
        apellido=apellido,
        dni=dni,
        telefono=telefono,
        email=email
    )
    empleado.save()
    return redirect('listaempleados')

# Eliminación de un empleado
class EmpleadosDeleteView(DeleteView):
    model = Empleado
    template_name = 'eliminar_empleado.html'
    success_url = reverse_lazy('listaempleados')

# Modificación de un empleado
class EmpleadosUpdateView(UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'modificar_empleado.html'
    success_url = reverse_lazy('listaempleados')

# Mostrar toda la lista de tareas, ordenadas por id
def pruebalistatarea(request):
    tareas = Tarea.objects.order_by('id')
    context = {
        'lista_tareas': tareas,
        'titulo_pagina': 'Listado de tareas'
    }
    return render(request, 'lista_tareas.html', context)

# Mostrar una tarea
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la tarea'
        context['titulo_pagina1'] = 'Detalles de la tarea'
        print(context)
        return context

# Creación de tareas
def show_form1(request):
    return render(request, 'crear_tarea.html')

def creartarea(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    inicio = request.POST["inicio"]
    fin = request.POST["fin"]
    responsable = request.POST["responsable"]
    prioridad = request.POST["prioridad"]
    estado = request.POST["estado"]
    notas = request.POST["notas"]

    tarea = Tarea(
        nombre=nombre,
        descripcion=descripcion,
        inicio=inicio,
        fin=fin,
        responsable=responsable,
        prioridad=prioridad,
        estado=estado,
        notas=notas
    )
    tarea.save()
    return redirect('listatareas')

# Eliminación de una tarea
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == "POST":
        tarea.delete()
        return redirect('listatareas')
    context = {
        "object": tarea,
        'titulo_pagina': 'Eliminación de tarea',
        'titulo_pagina1': 'Eliminar tarea'
    }
    return render(request, "eliminar_tarea.html", context)

# Mostrar toda la lista de proyectos, ordenados por id
def pruebalistaproyecto(request):
    proyectos = Proyecto.objects.order_by('id')
    context = {
        'lista_proyectos': proyectos,
        'titulo_pagina': 'Gestor de proyectos',
        'titulo_pagina1': 'Gestión de proyectos'
    }
    return render(request, 'lista_proyectos.html', context)

# Mostrar un proyecto
class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proyecto'
        context['titulo_pagina1'] = 'Detalles del proyecto'
        print(context)
        return context

# Creación de proyectos
from .forms import ProyectoForm

class CrearProyecto(View):
    def get(self, request, *args, **kwargs):
        form = ProyectoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear nuevo proyecto',
            'titulo_pagina1': 'Proyecto'
        }
        return render(request, 'crear_proyecto.html', context)

    def post(self, request, *args, **kwargs):
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaproyectos')
        return render(request, 'crear_proyecto.html', {
            'form': form,
            'titulo_pagina': 'Crear nuevo proyecto',
            'titulo_pagina1': 'Proyecto'
        })

# Eliminación de un proyecto
def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    if request.method == "POST":
        proyecto.delete()
        return redirect('listaproyectos')
    context = {
        "object": proyecto,
        'titulo_pagina': 'Eliminación de proyecto',
        'titulo_pagina1': 'Eliminar proyecto'
    }
    return render(request, "eliminar_proyecto.html", context)
