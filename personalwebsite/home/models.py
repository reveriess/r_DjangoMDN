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

class Education(models.Model):
    school_name=models.CharField(max_length=40)
    startdate=models.DateTimeField()
    enddate=models.DateTimeField()
    description=models.TextField()

    class Meta:
        ordering=['startdate']

    def __str__(self):
        return self.school_name

class Experiences(models.Model):
    exp_name=models.CharField(max_length=40)
    startdate=models.DateTimeField()
    enddate=models.DateTimeField()
    description=models.TextField()

    class Meta:
        ordering=['startdate']

    def __str__(self):
        return self.exp_name

class CurrentInterests(models.Model):
    interest_name=models.CharField(max_length=40)
    description=models.TextField()

    class Meta:
        ordering=['interest_name']

    def __str__(self):
        return self.interest_name