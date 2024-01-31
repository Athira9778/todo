from django.db import models

class Schedule(models.Model):
    title=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title
