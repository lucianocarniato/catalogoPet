from django.shortcuts import render


def cadastrarVeterinario(request):
    context = {}
    return render(request, 'cadastrar-veterinario.html', context)


def consultarVeterinario(request):
    context = {}
    return render(request, 'consultar-veterinario.html', context)


def editarVeterinario(request):
    context = {}
    return render(request, 'editar-veterinario.html', context)


def excluirVeterinario(request):
    context = {}
    return render(request, 'excluir-veterinario.html', context)
