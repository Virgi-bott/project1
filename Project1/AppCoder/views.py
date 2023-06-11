from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppCoder.forms import CursoFormulario, BuscaCursoForm, ProfesorFormulario

 
# Create your views here.
def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    
    return render(request, "AppCoder/entregables.html")

def formulario(request):
    if request.method == 'POST':
        
        curso = Curso(nombre = request.POST['curso'], camada = request.POST['camada'])
        
        curso.save()
        
        return render(request, "AppCoder/inicio.html")
    return render(request,"AppCoder/formulario.html")


def cursos(request):

    if request.method == "POST":

        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()
        
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})
        
def crear_profesor(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"],)
            profesor.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesorFormulario()
        
    return render(request, "AppCoder/formulario_profesor.html", {"miFormulario": miFormulario})

# def buscar_curso(request):
#     if request.method == "POST":
#         miFormulario = BuscaCursoForm(request.POST)
        
#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data
#             cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])
#             return render(request, "AppCoder/lista.html", {"cursos": cursos})
#     else:
#         miFormulario = BuscaCursoForm()
#         return render(request, "AppCoder/buscar_curso.html", {"miFormulario": miFormulario})

def busquedaCurso(request):
    return render(request, "AppCoder/buscar_curso.html")

def buscar(request):
    
    if request.GET['curso']:
        nombre = request.GET['curso']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "nombre": nombre})
    
    else:
        respuesta = "No enviaste datos"
    # respuesta = f"Estoy buscando el curso: {request.GET['curso']} "
    return render(request, "AppCoder/inicio.html", {"respuesta": respuesta })

def leerProfesores(request):
    
    profesores = Profesor.objects.all()
    
    contexto = {"profesores" : profesores}
    
    return render(request, "AppCoder/leerProfesores.html", contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesores = Profesor.objects.all()
    
    contexto = {"profesores": profesores}
    
    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion["nombre"]
            profesor.apellido = informacion["apellido"]
            profesor.email = informacion["email"]
            profesor.profesion = informacion["profesion"]
            profesor.save()
            return render(request, "AppCoder/inicio.html")
    
    else:
        miFormulario = ProfesorFormulario(initial={"nombre": profesor.nombre , "apellido":profesor.apellido , "email": profesor.email , "profesion": profesor.profesion})
        
    return render(request, "AppCoder/formulario_editar_profesor.html", {"miFormulario":miFormulario , "profesor_nombre":profesor_nombre})
        
         
    