from django.http import HttpResponse
#Permite mediante las funciones responder a las solicitudes que se
#realicen. Estas se dan a través de las palabras claves en la url.
from django.template import loader
from AppCoder.models import Curso,Familia


def home(request,name):
    return HttpResponse(f'Hola, soy la página de {name}')

def inicio(request):
    planilla = loader.get_template('inicio.html')
    documento = planilla.render()
    return HttpResponse(documento)
#Sin template.

def homePage(self):
    planilla = loader.get_template('home.html')
    documento = planilla.render()
    #Si tuviese datos que quiero que se plasmen en el renderizado del html
    #deberían ir como parámetro en el render, y obviamente figurar en el html como variables 
    #si es que quiero que aparezcan.
    return HttpResponse(documento)

def cursos(self):
    lista = [1,2,3,4]
    data = {'name':'Gonzalo','apellido':'Ferraro','Lista':lista}
    planilla = loader.get_template('cursos.html')
    documento = planilla.render(data)
    #Si tuviese datos que quiero que se plasmen en el renderizado del html
    #deberían ir como parámetro en el render, y obviamente figurar en el html como variables 
    #si es que quiero que aparezcan.
    return HttpResponse(documento)

def familia(self):
    Fam = Familia.objects.all()
    #Traer la data de la DB implica traer objetos, por lo que el contenido
    #del diccionario pasa a ser un conjunto de objetos que puedo iterar, y a cuya
    #información puedo acceder como a la de cualquier objeto con el '.' para conocer
    #sus "variables de instancia".
    dicc = {"Familia":Fam}
    #El contexto debe ser una lista, osea el data, o como quieras llamarlo.
    planilla = loader.get_template('familia.html')
    documento = planilla.render(dicc)
    return HttpResponse(documento)
