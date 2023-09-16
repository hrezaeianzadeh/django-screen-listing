from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

# Create your models here.
class Listing(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=120, blank=True, null=True)
    
    def __str__(self):
        return self.room_name

    def is_available(self, start_date: datetime, end_date: datetime):
        return not Reservation.objects.filter(start__lte=end_date, end__gte=start_date, room=self).exists()
    
    def is_available_at_time(self, certain_date: datetime):
        return not Reservation.objects.filter(start__lte=certain_date, end__gte=certain_date, room=self).exists()

class Reservation(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    holder_name = models.CharField(max_length=120)
    start = models.DateTimeField()
    end = models.DateTimeField()
    
    def __str__(self):
        return f"Reservation for room `{self.room.room_name}` under name `{self.holder_name}`"
