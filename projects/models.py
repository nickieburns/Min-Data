from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField() #github
    body = models.TextField()

    last_modified = models.DateField(auto_now_add=True)
    complete = models.BooleanField()

    def __str__(self):
        return self.title
