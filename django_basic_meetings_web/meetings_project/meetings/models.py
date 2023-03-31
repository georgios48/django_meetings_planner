from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    # Display info
    def __str__(self):
        return f"{self.name}: room {self.room_number} on {self.floor} floor."

    objects = models.Manager()


class Meetings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.IntegerField(default=time(9))  # Hours
    duration = models.IntegerField(default=1)

    # If a room is deleted, CASCADE deletes its settings
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

    # Verbose name plural
    class Meta:
        verbose_name_plural = 'Meetings'

    objects = models.Manager()

# Create your models here.
