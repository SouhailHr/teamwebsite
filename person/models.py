from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=300)
    title = models.CharField(max_length=100)
    Linkedin_url = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        return self.email

    class Meta:
        ordering = ['-created']
        ordering = ['-updated']
