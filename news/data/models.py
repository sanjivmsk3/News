from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40,unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Headline(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    time = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/')
    slug = models.SlugField()

    def __str__(self):
        return self.name
