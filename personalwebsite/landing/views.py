from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Year, Experiences, StoryPost, Education, Timeline

# Create your views here.
def homeview(request):
    post = StoryPost.objects.all()
    educations = Education.objects.all()
    experiences = Experiences.objects.all()

    year = Year.objects.all()
    timeline = Timeline.objects.all()
    print(timeline)
    print(year)
    arg = {
        "posts": post,
        "educations": educations,
        "experiences": experiences,
        "timeline": timeline,
        "year": year,
    }
    return render(request, "landing.html", arg)
