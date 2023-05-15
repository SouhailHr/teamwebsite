from django.db import models


# Create your models here.
class Project(models.Model):
    description = models.TextField(max_length=1000)
    overview = models.TextField(max_length=500)
    title = models.CharField(max_length=100)
    tools = models.CharField(max_length=200)
    Link = models.CharField(max_length=200)
    dashbord_image = models.ImageField(upload_to='images/%y/%m/%d/', max_length=255, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        return self.link

    class Meta:
        ordering = ['-created']
        ordering = ['-updated']