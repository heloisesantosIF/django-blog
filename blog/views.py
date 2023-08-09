from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})
def ola(request):
    #return HttpResponse('Olá Django')
    return render(request, 'home.html')