from django.db import models

class Liste(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)