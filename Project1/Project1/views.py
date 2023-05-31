from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
	return HttpResponse("“Hola Django - Coder”")

def bienvenida(self, nombre):
    texto = f"Bienvenido {nombre}"
    return HttpResponse(texto)

def probandoTemplate(self):
    miHtmal = open(r"C:\Users\Vir\Documents\Python\PythonProjecto1\Project1\Project1\Plantillas\template1.html")
    plantilla = Template(miHtmal.read())
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)