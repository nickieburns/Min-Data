from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField() #mostly youtube
    body = models.TextField()

    ancillary_materials = models.TextField() #references, etc.
    last_modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
