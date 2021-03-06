from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    """
    The Blog homepage
    """
    # Get last 3 posts
    latest_posts = models.Post.objects.published().order_by('-published')[:3]
    authors = models.Post.objects.published().get_authors().order_by('first_name')

    # Add as context variable "latest_posts"
    context = {
        'authors': authors,
        'latest_posts': latest_posts
    }

    return render(request, 'blog/home.html', context)
