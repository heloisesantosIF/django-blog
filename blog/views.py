#primeiro do python
import json
#dps do django
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
#oq é nosso
from blog.models import Post
from blog.forms import PostModelForm


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

def get_all_posts(request):
    posts = list(Post.objects.values('pk', 'body_text', 'pub_date'))
    data = {'success': True, 'posts': posts}
    json_data = json.dumps(data, indent=1, cls=DjangoJSONEncoder)
    response = HttpResponse(json_data, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    return response

def get_post(request, post_id):
    post = Post.objects.filter(
        pk=post_id
    ).values(
        'pk', 'body_text', 'pub_date'
    ).first()

    data = {'success': True, 'post': post}
    status = 200
    if post is None:
        data = {'success': False, 'error': 'Post ID não existe.'}
        status=404

    response = HttpResponse(
        json.dumps(data, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
        status=status
    )
    
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    return response

class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_form.html'
    #fields = ('body_text', )
    success_url = reverse_lazy('posts_list')
    form_class = PostModelForm

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        body_text = data.get('body_text')
        if body_text is None:
            data = {'success': False, 'error': 'Texto do post inválido.'}
            status = 4000 # Bad Request => erro do client
        else:
            post = Post(body_text=body_text)
            post.save()
            post_data = Post.objects.filter(
                pk=post.id
            ).values(
                'pk', 'body_text', 'pub_date'
            ).first()
            data = {'success': True, 'post': post_data}
            status = 201 # Created
        response = HttpResponse(
            json.dumps(data, indent=1, cls=DjangoJSONEncoder),
            content_type="application/json",
            status=status
        )
        response['Access-Control-Allow-Origin'] = '*'
        return response
    
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

class SobreTemplateView(TemplateView):
    template_name = 'post/sobre.html'

