from django.shortcuts import render


def consultarInstituicao(request):
    context = {}
    return render(request, 'consultar-instituicao.html', context)


def excluirInstituicao(request):
    context = {}
    return render(request, 'deletar-instituicao.html', context)


def editarInstituicao(request):
    context = {}
    return render(request, 'editar-instituicao.html', context)


def cadastrarInstituicao(request):
    context = {}
    return render(request, 'cadastrar-instituicao.html', context)
