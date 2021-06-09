from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'dantup01',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'Wed 9th June'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
