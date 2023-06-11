from django.urls import path
from AppCoder import views, view



urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path("cursos", views.cursos, name="Cursos"),
    path("profesores", views.profesores, name="Profesores"),
    path("estudiantes", views.estudiantes, name="Estudiantes"),
    path("entregables", views.entregables, name="Entregables"),
    path("formulario", views.formulario, name="Formulario"),
    path("form-api", views.cursos, name="Form-api"),
    path("crear_profesor", views.crear_profesor, name="Crear_profesor"),
    path("buscar_curso", views.busquedaCurso, name="Buscar-curso"),
    path("buscar", views.buscar),
    path("leerProfesores", views.leerProfesores, name="LeerProfesores"),
    path("eliminarProfesor/<profesor_nombre>/", views.eliminarProfesor, name="EliminarProfesor"),
    path("editarProfesor/<profesor_nombre>/", views.editarProfesor, name="EditarProfesor"),
    path("curso/list", view.CursoListView.as_view(), name = "List"),
    path(r'^(?P<pk>\d+)$', view.CursoDetailView.as_view(), name = "Detail"),
    path(r'^nuevo$', view.CursoCreateView.as_view(), name = "New"),
    path(r'^editar/(?P<pk>\d+)$', view.CursoUpdateView.as_view(), name = "Edit"),
    path(r'^borrar/(?P<pk>\d+)$', view.CursoDeleteView.as_view(), name = "Delete"),
    
]