from django.shortcuts import render
from .models import Proyecto



def index(request):
    template_name="index.html"
    #Lista
    proyectos = [
        Proyecto("Proyecto1","Descripcion del Proyecto 1","1.png",120),
        Proyecto("Proyecto2","Descripcion del Proyecto 2","2.png",180),
        Proyecto("Proyecto3","Descripcion del Proyecto 3","3.png",200),
        Proyecto("Proyecto4","Descripcion del Proyecto 4","4.png",140)
        #Agregar mas proyectos segun sea necesario
    ]
    context = {
        'proyectos':proyectos
    }
    return render(request,template_name,context)





