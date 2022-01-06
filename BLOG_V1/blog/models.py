from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=300)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])
    
    def __str__(self):
        return self.title


    