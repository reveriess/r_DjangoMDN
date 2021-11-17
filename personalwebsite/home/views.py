from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import StoryPost, Education, Experiences, CurrentInterests

# Create your views here.
def homeview(request):
    post = StoryPost.objects.all()
    arg = {"posts": post}
    return render(request, "template_post.html", arg)


def aboutme(request):
    education = Education.objects.all()
    experience = Experiences.objects.all()
    currentinterest = CurrentInterests.objects.all()
    arg = {
        "education": education,
        "experience": experience,
        "currentinterest": currentinterest,
    }
    return render(request, "aboutme.html", arg)


def stories(request, page):
    stories_per_page = 3
    post = StoryPost.objects.order_by("date").all()[
        (page - 1) * stories_per_page : page * stories_per_page
    ]
    arg = {"posts": post,"show_button":True}
    return render(request, "template_stories.html", arg)
