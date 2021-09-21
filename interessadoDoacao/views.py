from django.shortcuts import render


def cadastrarInteressado(request):
    context = {}
    return render(request, 'cadastrar-interessado.html', context)


def consultarInteressado(request):
    context = {}
    return render(request, 'consultar-interessado.html', context)


def excluirInteressado(request):
    context = {}
    return render(request, 'deletar-interessado.html', context)


def editarInteressado(request):
    context = {}
    return render(request, 'exclusao-interessado.html', context)
     