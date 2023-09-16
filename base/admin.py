from django.contrib import admin
from .models import Reservation, Listing, Room

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    
    list_display = ('uid', 'holder_name', 'room', 'start', 'end')
    list_filter = ('start', 'end')
    
    fields = ('uid', 'holder_name', 'room', 'start', 'end')
    readonly_fields = ('uid',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    model = Room
    
    list_display = ('uid', 'room_name', 'listing')
    list_filter = ('listing',)
    
    fields = ('uid', 'room_name', 'listing')
    readonly_fields = ('uid',)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    model = Listing
    
    list_display = ('uid', 'name', 'owner')
    list_filter = ('owner',)
    
    fields = ('uid', 'name', 'owner')
    readonly_fields = ('uid',)
    
    
