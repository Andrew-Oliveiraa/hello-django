from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello World</h1>')
def person(request, nome, idade):
    return HttpResponse('<h1>Página de teste person: nome=>{} idade=>{}<h1>'.format(nome,idade))
def teste(request,nome_teste):
    return HttpResponse('Teste de : {}'.format(nome_teste))
