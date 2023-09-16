from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reservation, Room, Listing

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    owner = UserSerializer(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = Listing
        fields = ('uid', 'owner', 'name')
        read_only_fields = ('uid', 'owner',)

class RoomSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    room_name = serializers.CharField(allow_null=True, required=False)
    listing = ListingSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('uid', 'room_name', 'listing')
        read_only_fields = ('uid', 'listing',)

class ReservationSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    room = RoomSerializer(read_only=True)
    holder_name = serializers.CharField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()

    class Meta:
        model = Reservation
        fields = ('uid', 'room', 'holder_name', 'start', 'end')
        read_only_fields = ('uid',)
