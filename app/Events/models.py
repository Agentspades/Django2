from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    maxAttendees = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1)])
    description = models.TextField()
    location = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    date = datetime.now().strftime('%Y-%m-%d')
    imageLink = models.FileField(upload_to=f'uploads/{date}/', blank=True)

    class Meta:
        db_table = 'events'
        verbose_name_plural = 'Events'

    def __str__(self):
        return str(self.name)


class EventRegistration(models.Model):
    eventID = models.ForeignKey(
        'Event', on_delete=CASCADE, db_column='eventID', default=0, verbose_name='Event')
    userID = models.ForeignKey(
        'Auth.User', on_delete=CASCADE, db_column='userID', default=0, verbose_name='Email')
    attendees = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        db_table = 'registrations'
        verbose_name_plural = 'Registrations'

    def __str__(self):
        return str(self.userID)
