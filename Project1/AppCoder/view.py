from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

class CursoListView(ListView):
    model = Curso
    template_name = "AppCoder/cursos_list.html"
    
class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"
    
class CursoCreateView(CreateView):
    model = Curso
    success_url = "AppCoder/curso/list"
    fields = ['nombre', 'camada']
    
class CursoUpdateView(UpdateView):
    model = Curso
    success_url = "AppCoder/curso/list"
    fields = ['nombre', 'camada']
    
class CursoDeleteView(DeleteView):
    model = Curso
    success_url = "AppCoder/curso/list"
    