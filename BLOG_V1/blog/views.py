from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# blog_posts = {
#     "the first one": "blogging is the coolest I alwys enjoy lettem know whats going on upstairs!",
#     "the second one": "look another blog post!",
#     "the third one": "hey im just doing my best out here",
#     "the fourth one": "what the heck is going on here?",
# }

# # Create your views here.
# def home(request):
#     latest_title = list(blog_posts.keys())
#     latest_text = list(blog_posts.values())
    
#     return render(request, "blog/home.html", {'blog_title': latest_title, 'blog_text': latest_text})


# def index(request):
#     blog_list = list(blog_posts.keys())
#     return render(request, "blog/index.html", {"blog_list": blog_list})


# def details_by_number(request, blog):
#     blogs = list(blog_posts.keys())
#     if blog > len(blogs):
#         return HttpResponseNotFound("Invalid number")
#     redirect_blog = blogs[blog - 1]
#     redirect_path = reverse("details", args=[redirect_blog])
#     return HttpResponseRedirect(redirect_path)


# def details(request, blog):
#     try:
#         blog_text = blog_posts[blog]
#         return render(
#             request, "blog/details.html", {"text": blog_text, "blog_name": blog}
#         )
#     except:
#         raise Http404()

def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    return render(request, 'blog/index.html')

def post_detail(request):
    pass

