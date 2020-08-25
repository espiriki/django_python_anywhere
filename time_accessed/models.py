from django.db import models

class TimeAcessed(models.Model):
    formatted_date = models.CharField(max_length=200)

    def __str__(self):
        return self.formatted_date
