from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]  # combined with global default
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['status','author__username']  # exact filtering
    search_fields = ['title','body']                 # full text-like search
    ordering_fields = ['created','updated','title']
    ordering = ['-created']

    def perform_create(self, serializer):
        # set the author to the logged in user
        serializer.save(author=self.request.user)

