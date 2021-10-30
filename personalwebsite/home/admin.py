from django.contrib import admin
from .models import StoryPost,Education,Experiences,CurrentInterests
# Register your models here.
admin.site.register(StoryPost)
admin.site.register(Education)
admin.site.register(Experiences)
admin.site.register(CurrentInterests)