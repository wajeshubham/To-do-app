from django.db import models


# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=500)
    added_date = models.DateTimeField()

    def __str__(self):
        return self.task
