from base.models import Listing, Room, Reservation, User
from datetime import datetime, timedelta
import pytz

owner_1 = User.objects.create_user(username='owner1', email='owner1@listing.com', password='secret')
owner_2 = User.objects.create_user(username='owner2', email='owner2@listing.com', password='secret')

listing_1 = Listing.objects.create(owner=owner_1, name='Listing 1')
listing_2 = Listing.objects.create(owner=owner_2, name='Listing 2')

room_1 = Room.objects.create(listing=listing_1, room_name='Room 1')
room_2 = Room.objects.create(listing=listing_1, room_name='Room 2')
room_3 = Room.objects.create(listing=listing_1, room_name='Room 3')

room_4 = Room.objects.create(listing=listing_2, room_name='Room 4')
room_5 = Room.objects.create(listing=listing_2, room_name='Room 5')
room_6 = Room.objects.create(listing=listing_2, room_name='Room 6')

start_date = datetime.now(tz=pytz.UTC)
end_date = start_date + timedelta(days=2)
reservation_1 = Reservation.objects.create(room=room_4, holder_name='test_holder', start=start_date, end=end_date)