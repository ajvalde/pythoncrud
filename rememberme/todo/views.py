from django.shortcuts import render
from .models import Post
# Create your views here.

def list_of_post(request):
    post = Post.objects.all()
    template = 'list_of_posts.html'
    context = {'post': post}
    return render(request, template, context)
