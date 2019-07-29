from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Author
from .forms import PostModelForm
from django.contrib import messages

# Create your views here.
def posts_list(request):
    all_posts = Post.objects.all()
    context = {
    'all_posts' : all_posts
    }
    messages.info(request, 'Here are all the blog posts')
    return render(request, 'posts_list.html', context)

def post_detail(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    context = {
    'post':unique_post
    }
    messages.info(request, 'This is the detail view')
    return render(request, 'post_detail.html', context)


def posts_create(request):
    author, created = Author.objects.get_or_create(
    user = request.user,
    email = request.user.email,
    phone = 1234566
    )
    form = PostModelForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        form.instance.author =author
        form.save()
        return redirect('/posts/')
    context = {
    'form':form
    }
    messages.info(request, 'Successfully created a new blog post')
    return render(request, 'post_create.html', context)

def posts_update(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    form = PostModelForm(request.POST or None, request.FILES or None, instance=unique_post)
    if form.is_valid():
        form.save()
        return redirect('/posts/')
    context = {
    'form':form
    }
    messages.info(request, 'Successfully updated your blog post')
    return render(request, 'post_create.html', context)


def posts_delete(request, slug):
    unique_post = get_object_or_404(Post, slug=slug)
    unique_post.delete()
    messages.info(request, 'Successfully deleted your blog post')
    return redirect('/posts/')
