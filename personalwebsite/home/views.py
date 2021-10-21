from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import StoryPost
# Create your views here.
def homeview(request):
    post=StoryPost.objects.all()
    arg={'posts':post}
    return render(request,'template_post.html',arg)

def aboutme(request):
    return render(request,'aboutme.html')

def stories(request,page):
    stories_per_page=3;
    post=StoryPost.objects.order_by('date').all()[(page-1)*stories_per_page:page*stories_per_page]
    arg={'posts':post}
    return render(request,'template_stories.html',arg)