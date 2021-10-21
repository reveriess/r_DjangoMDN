from django.db import models

# Create your models here.
class StoryPost(models.Model):
    text=models.TextField()
    date=models.DateTimeField()
    title=models.CharField(max_length=40)
    summary=models.TextField()

    class Meta:
        ordering=['date']

    def __str__(self):
        return self.title