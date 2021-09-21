from django.urls import path
from .import views

urlpatterns = [
    path('cadastrar/', views.cadastrarVeterinario, name='cadastrar-veterinario'),
    path('consultar/', views.consultarVeterinario, name='consultar-veterinario'),
    path('excluir/', views.excluirVeterinario, name='excluir-veterinario'),
    path('editar/', views.editarVeterinario, name='editar-veterinario'),
]
