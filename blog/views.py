from django.shortcuts import render

from django.http import HttpResponse
from blog.models import Post

def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})
def ola(request):
    #return HttpResponse('Olá Django')
    posts = Post.objects.all()
    context = {'posts_list': posts } 
    return render(request, 'posts.html', context)
    #return render(request, 'home.html')