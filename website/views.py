from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost

def website(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'website.html', {'blog_posts': blog_posts})

@login_required(login_url="/login/")
def post_blog(request):
  if request.method == 'POST':
    heading = request.POST.get('heading')
    category = request.POST.get('category')
    content = request.POST.get('content')
    blog_photo = request.FILES.get('blog_photo')
    date = request.POST.get('date')
    
    BlogPost.objects.create(
      author=request.user,
      heading=heading,
      category=category,
      content=content,
      blog_photo=blog_photo,
      date=date
    )
    return redirect('website')
  return render(request, 'blog_post.html')

from django.shortcuts import render, get_object_or_404
from .models import *

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})
