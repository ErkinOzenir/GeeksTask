from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Task'

    def __str__(self):
        return self.title
