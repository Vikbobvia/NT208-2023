from django.db import models

# Create your models here.

class Text_table(models.Model):
    date = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)