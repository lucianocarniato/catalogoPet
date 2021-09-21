from django.shortcuts import render


def cadastrarPet(request):
    context = {}
    return render(request, 'cadastrar-pet.html', context)


def consultarPet(request):
    context = {}
    return render(request, 'consultar-pet.html', context)


def editarPet(request):
    context = {}
    return render(request, 'editar-pet.html', context)


def excluirPet(request):
    context = {}
    return render(request, 'excluir-pet.html', context)
