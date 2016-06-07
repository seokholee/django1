from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.all()
