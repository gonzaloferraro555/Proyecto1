from django.shortcuts import render
from django.http import response
#Necesito el responde y el render para mostrar los html.

#Comenzamos a usar el render en lugar del
#loader, ver como funciona
def inicio(request):
    return render(request,"inicio2.html")



def cursos(request):
    return render(request,"cursos2.html")



def estudiantes(request):
    return render(request,"estudiantes.html")
#Es una función por cada página



def profesores(request):
    return render(request,"profesores.html")



def entregables(request):
    return render(request,"entregables.html")
#min 50:47 de django 3



def home(request):
    return render(request,"home2.html")
# Create your views here.
