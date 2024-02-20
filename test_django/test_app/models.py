from django.db import models

class Performer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])
    title = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.title
