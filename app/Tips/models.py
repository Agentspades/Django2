from django.db import models

# Create your models here.


class TipModel(models.Model):
    tip = models.TextField()
    date = models.DateField()

    class Meta:
        db_table = 'tips'
        verbose_name_plural = 'Weekly Tips'
        get_latest_by = ['id']

    def __str__(self):
        return self.tip
