from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    test_no = models.IntegerField(default=0)

    def __str__(self):
        return self.title
