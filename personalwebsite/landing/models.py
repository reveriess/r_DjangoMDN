from django.db import models

# Create your models here.
class StoryPost(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    title = models.CharField(max_length=40)
    summary = models.TextField()

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title


class Education(models.Model):
    school_name = models.CharField(max_length=40)
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ["-startdate"]

    def __str__(self):
        return self.school_name


class Experiences(models.Model):
    exp_name = models.CharField(max_length=40)
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ["-startdate"]

    def __str__(self):
        return self.exp_name


class CurrentInterests(models.Model):
    interest_name = models.CharField(max_length=40)
    description = models.TextField()

    class Meta:
        ordering = ["interest_name"]

    def __str__(self):
        return self.interest_name


class StravaAPI(models.Model):
    code = models.TextField(blank=True)

    def __str__(self):
        return self.code


class Year(models.Model):
    year = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.year)


class Timeline(models.Model):
    text = models.TextField()
    prio = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        ordering = ["prio"]

    def __str__(self):
        return self.text


@classmethod
def model_field_exists(cls, field):
    try:
        cls._meta.get_field(field)
        return True
    except models.FieldDoesNotExist:
        return False


models.Model.field_exists = model_field_exists
