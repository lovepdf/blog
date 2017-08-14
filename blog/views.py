from django.shortcuts import render
from blog.models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    # print posts
    return render(request, 'blog/post_list.html', {'posts':posts})