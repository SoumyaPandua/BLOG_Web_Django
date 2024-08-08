from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from website.models import BlogPost
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
def admin_dash(request):
    bloggers = User.objects.filter(role='blogger')
    blog_posts = BlogPost.objects.all()  # Fetch all blog posts

    bloggers_data = []
    for blogger in bloggers:
        post_count = BlogPost.objects.filter(author=blogger).count()
        bloggers_data.append({
            'blogger': blogger,
            'post_count': post_count,
        })

    return render(request, "admin.html", {
        'bloggers_data': bloggers_data,
        'blog_posts': blog_posts  # Pass blog posts to the template
    })



@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        post.heading = request.POST['heading']
        post.category = request.POST['category']
        post.content = request.POST['content']
        post.date = request.POST['date']

        if 'blog_photo' in request.FILES:
            post.blog_photo = request.FILES['blog_photo']

        post.save()
        return redirect('admin')

    return render(request, 'edit_blog.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('admin')

    return render(request, 'delete_blog.html', {'post': post})


@login_required
def manage_bloggers(request):
    bloggers = User.objects.filter(role='blogger')
    return render(request, 'manage_bloggers.html', {'bloggers': bloggers})


@login_required
def edit_blogger(request, blogger_id):
    blogger = get_object_or_404(User, id=blogger_id, role='blogger')

    if request.method == 'POST':
        blogger.first_name = request.POST['first_name']
        blogger.last_name = request.POST['last_name']
        blogger.email = request.POST['email']
        blogger.save()
        return redirect('manage_bloggers')

    return render(request, 'edit_blogger.html', {'blogger': blogger})

@login_required
def delete_blogger(request, blogger_id):
    blogger = get_object_or_404(User, id=blogger_id, role='blogger')

    if request.method == 'POST':
        blogger.delete()
        return redirect('manage_bloggers')

    return render(request, 'delete_blogger.html', {'blogger': blogger})
