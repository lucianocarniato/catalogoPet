from django.urls import path
from .import views

urlpatterns = [
    path('cadastrar/', views.cadastrarPet, name='cadastrar-pet'),
    path('consultar/', views.consultarPet, name='consultar-pet'),
    path('editar/', views.editarPet, name='editar-pet'),
    path('excluir/', views.excluirPet, name='excluir-pet'),
]
    
