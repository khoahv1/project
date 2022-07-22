from django.db import models
# Create your models here.


class Nguoidung(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.username