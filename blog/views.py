from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views.generic.detail import DetailView
from blog.models import Post

def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})
def ola(request):
    #return HttpResponse('Olá Django')
    posts = Post.objects.all()
    context = {'posts_list': posts } 
    return render(request, 'posts.html', context)
    #return render(request, 'home.html')

def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'
