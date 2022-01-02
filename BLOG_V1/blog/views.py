from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

blog_posts = {
    "the first one": "blogging is the coolest I alwys enjoy lettem know whats going on upstairs!",
    "the second one": "look another blog post!",
    "the third one": "hey im just doing my best out here",
}

# Create your views here.
def home(request):
    pass


def index(request):
    blog_list = list(blog_posts.keys())
    return render(request, "blog/index.html", {"blog_list": blog_list})

def details_by_number(request, blog):
    blogs = list(blog_posts.keys())
    if blog > len(blogs):
        return HttpResponseNotFound('Invalid number')
    redirect_blog = blogs[blog - 1]
    redirect_path = reverse( 'details', args=[redirect_blog])
    return HttpResponseRedirect(redirect_path)

def details(request, blog):
    try:
        blog_text = blog_posts[blog]
        return render(request, 'blog/details.html', {'text': blog_text, 'blog_name': blog})
    except:
        raise Http404()