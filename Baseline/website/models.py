from django.db import models
import datetime

# Create your models here.

class Text_table(models.Model):
    date = models.CharField(max_length=30)
    description = models.TextField(max_length=30000000000000)
    title = models.CharField(default="123", max_length=200)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    