from django.urls import path
from . import views

urlpatterns = [
    path('consultar/', views.consultarInstituicao, name='consultar-instituicao'),
    path('excluir/', views.excluirInstituicao, name='excluir-instituicao'),
    path('editar/', views.editarInstituicao, name='editar-instituicao'),
    path('cadastrar/', views.cadastrarInstituicao, name='cadastrar-instituicao'),
]
