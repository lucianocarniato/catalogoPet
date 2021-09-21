from django.urls import path
from .import views

urlpatterns = [
    path('cadastrar/', views.cadastrarInteressado, name='cadastrar-interessado'),
    path('consultar/', views.consultarInteressado, name='consultar-interessado'),
    path('excluir/', views.excluirInteressado, name='excluir-interessado'),
    path('editar/', views.editarInteressado, name='editar-interessado'),
]
