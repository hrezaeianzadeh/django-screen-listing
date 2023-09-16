from django.http import JsonResponse
from django.core import serializers
from rest_framework import status
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Reservation, Room, Listing
from base.serializers import RoomSerializer
from datetime import datetime
import json

# Create your views here.
@api_view(['GET'])
def getRoutes(request: HttpRequest):
    routes = [
        'api/check',
        'api/reservation'
    ]
    return Response(routes)

@api_view(['POST'])
def checkAvailableRooms(request: HttpRequest):
    try:
        start = request.data['start']
        date_range = True
        try:
            end = request.data['end']
        except Exception as e:
            date_range = False
        
        available_rooms = []   
        for room in Room.objects.all():
            if date_range and room.is_available(start_date=start, end_date=end):
                available_rooms.append(room)
            elif room.is_available_at_time(certain_date=start):
                available_rooms.append(room)
        response = {}
        for i, room in zip(range(len(available_rooms)), available_rooms):
            response[i] = {
                'Room name': room.room_name,
                'Listing': room.listing.name,
            }
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def overview(request: HttpRequest):
    try:
        listing_name = request.data['listing_name']
        listing = Listing.objects.filter(name=listing_name)[0]
        reservations = Reservation.objects.filter(room__listing=listing)
        response = {}
        for i, r in zip(range(len(reservations)), reservations):
            response[i] = {
                "Room name": r.room.room_name,
                "Reservation holder": r.holder_name,
                "Check-in date": r.start,
                "Check-out date": r.end
            }
        return Response(data=response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)