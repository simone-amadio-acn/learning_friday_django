from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Novel(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    body = models.CharField(max_length=2048)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title