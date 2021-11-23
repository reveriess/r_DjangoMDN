from django.contrib import admin
from .models import (
    Year,
    StoryPost,
    Education,
    Experiences,
    CurrentInterests,
    StravaAPI,
    Timeline,
)

# Register your models here.
admin.site.register(StoryPost)
admin.site.register(Education)
admin.site.register(Experiences)
admin.site.register(CurrentInterests)
admin.site.register(StravaAPI)
admin.site.register(Timeline)
admin.site.register(Year)
