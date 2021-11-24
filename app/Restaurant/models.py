from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class RestaurantBooking(models.Model):
    userID = models.ForeignKey(
        "Auth.User", on_delete=CASCADE, db_column='userID', default=0, verbose_name='User')
    phone = models.CharField(max_length=10)
    guests = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'restaurantBookings'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return str(self.userID)
