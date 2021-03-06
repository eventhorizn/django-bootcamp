from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def starting_page(request):
    # Django converts the entire line to a query
    # It doesn't get all the rows then slices the last 3
    latest_posts = Post.objects.all().order_by('-date')[:3]

    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")

    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    found_post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post-detail.html', {
        'post': found_post,
        'post_tags': found_post.tags.all()
    })
