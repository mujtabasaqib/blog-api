from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'), ('published','Published'))
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

