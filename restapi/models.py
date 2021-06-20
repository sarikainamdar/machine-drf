from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    created_by = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'