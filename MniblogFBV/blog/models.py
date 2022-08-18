from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.CharField(max_length=555)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    phone_num = models.PositiveIntegerField()
    content = models.TextField(max_length=155)

    def __str__(self) -> str:
        return self.name
