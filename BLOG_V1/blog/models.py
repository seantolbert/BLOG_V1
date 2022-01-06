from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    date = models.DateField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=300)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])
    
    def __str__(self):
        return self.title


    