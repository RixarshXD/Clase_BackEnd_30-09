from django.shortcuts import render, redirect
from APP1.models import Proyecto
from APP1.form import FormProyecto
# Create your views here.

def index(request):
    return render(request,'index.html')

def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos' : proyectos}
    return render(request,'proyectos.html', data)

def agregarProyectos(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
            return listadoProyectos(request) 
        else:
            print(form.errors)
    data = {'form' : form}
    return render(request, 'agregarProyectos.html', data)

# eliminar proyectos
def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return redirect('/proyectos')


def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return listadoProyectos(request)
    data = {'form' : form}
    return render(request, 'agregarProyectos.html', data) 


