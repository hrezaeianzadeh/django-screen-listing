from django.test import TestCase, AsyncClient
from rest_framework.test import APIRequestFactory, APITestCase
from .models import Reservation, Room, Listing, User
from datetime import datetime, timedelta
import pytz
import json

# Create your tests here.
class ReservationTestCase(APITestCase):
    def setUp(self) -> None:
        self.test_owner = User.objects.create_user(username='test_owner', email='test_owner@listing.com', password='secret')
        self.test_listing = Listing.objects.create(owner=self.test_owner, name='Test Listing')
        self.test_room_1 = Room.objects.create(room_name='Test Room 1', listing=self.test_listing)
        self.test_room_2 = Room.objects.create(room_name='Test Room 2', listing=self.test_listing)
    
    def test_make_reservation(self):
        start_date = datetime.now(tz=pytz.UTC)
        end_date = start_date + timedelta(days=2)
        data = {
            "room": str(self.test_room_1.uid),
            "holder_name": "test_holder",
            "start": str(start_date),
            "end": str(end_date),
        }
        response = self.client.post('/api/reservation/', data=data)
        self.assertEqual(200, response.status_code)
    
    def test_available_rooms(self):
        start_date = datetime.now(tz=pytz.UTC)
        end_date = start_date + timedelta(days=2)
        
        data = {
            "room": str(self.test_room_1.uid),
            "holder_name": "test_holder",
            "start": str(start_date),
            "end": str(end_date),
        }
        response = self.client.post('/api/reservation/', data=data)
        self.assertEqual(200, response.status_code)
        
        data = {
            "start": str(start_date),
            "end": str(end_date),
        }
        response = self.client.post('/api/check/', data=data)
        self.assertEqual(200, response.status_code)
        
        # test_room_1 should not be available
        response_contains_test_room_1 = False
        for k, v in response.data.items():
            if v['Room name'] == 'Test Room 1':
                response_contains_test_room_1 = True
        self.assertFalse(response_contains_test_room_1)
        