from django.db import models

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

class Posts(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
