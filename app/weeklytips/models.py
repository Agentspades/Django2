from django.db import models

# Create your models here.


class SustainableTips(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=700)
    date_added = models.DateField(blank=True)

    class Meta:
        db_table = 'weeklyTips'
        verbose_name_plural = 'Weekly Tips'

    def __str__(self):
        return self.Title
