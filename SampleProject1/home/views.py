from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about-me.html')
def recent(request):
    return render(request,'recent-posts.html')
def index(request):
    data={'blog':Blog.objects.all()}
    return render(request,'index.html',data)
