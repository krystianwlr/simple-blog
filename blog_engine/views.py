from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog_engine/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_engine/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # to save post as a draft
            #post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('blog_engine:post_detail', args=[post.id]))
    else:
        form = PostForm()
    return render(request, 'blog_engine/post_edit.html', {'form': form})

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # to save post as a draft
            #post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('blog_engine:post_detail', args=[post.id]))
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_engine/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog_engine/post_draft_list.html', {'posts': posts})

def post_publish(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.publish()
    return render(request, 'blog_engine/post_detail.html', {'post': post})

def post_remove(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    response = post_list(request)
    return response