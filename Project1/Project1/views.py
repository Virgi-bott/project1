from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader


def saludo(request):
	return HttpResponse("“Hola Django - Coder”")

def bienvenida(self, nombre):
    texto = f"Bienvenido {nombre}"
    return HttpResponse(texto)

def probandoTemplate(self):
    nombre = "Bebito"
    apellido = "Fiu fiu"
    dicc = {"nombre":nombre , "apellido":apellido}
    # miHtmal = open(r"C:\Users\Vir\Documents\Python\PythonProjecto1\Project1\Project1\Plantillas\template1.html")
    # plantilla = Template(miHtmal.read())
    # miHtmal.close()
    # miContexto = Context(dicc)
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)