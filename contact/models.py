from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=50)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
        return self.company

    class Meta:
        ordering = ['-created']
