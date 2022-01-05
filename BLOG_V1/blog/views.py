from django.shortcuts import render
from django.urls import reverse
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "crusty_butt.jpg",
        "author": "Sean Tolbert",
        "date": date(2022, 1, 4),
        "title": "Mountain Hiking",
        "excerpt": "There was once a long ass striung that deserved to be thrown into a large paragraph format",
        "content": """
        Lore;asjnbdvejnvoeifnb'oeinb'eonb'ek
    'ngwo;ernb[oweirng'irng'pqrng'pewkrn'lweknb
    'qeppkrgn'werng'pewinb'ekbn'lrkgnbdflkjgnbskdljfbnslkdfjbvklsdjb
    """,
    },
    {
        "slug": "riding-the-edge",
        "image": "vale_backside.jpg",
        "author": "Sean Tolbert",
        "date": date(2021, 12, 14),
        "title": "Riding The Edge",
        "excerpt": "I have really struggled with hoe to justify the views we have up here. Pictures and raw perspective have been my only outlets, but I know there is so much more.",
        "content": """
        Lore;asjnbdvejnvoeifnb'oeinb'eonb'ek
    'ngwo;ernb[oweirng'irng'pqrng'pewkrn'lweknb
    'qeppkrgn'werng'pewinb'ekbn'lrkgnbdflkjgnbskdljfbnslkdfjbvklsdjb
    """,
    },
    {
        "slug": "painful-hikes",
        "image": "shavano.jpg",
        "author": "Sean Tolbert",
        "date": date(2021, 4, 15),
        "title": "Painful Hikes",
        "excerpt": "still trying to figure out how I crushhed this without passing out.",
        "content": """
        Lore;asjnbdvejnvoeifnb'oeinb'eonb'ek
    'ngwo;ernb[oweirng'irng'pqrng'pewkrn'lweknb
    'qeppkrgn'werng'pewinb'ekbn'lrkgnbdflkjgnbskdljfbnslkdfjbvklsdjb
    """,
    },
]

def get_date(post):
    return post['date']

def home(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        'posts': latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        'all_posts': all_posts,
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/details.html", {
        'post': identified_post,
    })
