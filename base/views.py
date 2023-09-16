from django.contrib.auth.models import User
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.db import transaction
from .serializers import UserSerializer, ReservationSerializer
from .models import Reservation, Listing, Room
from datetime import datetime
from asgiref.sync import sync_to_async

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)

    def get_object(self):
        return self.request.user

    def retrieve(self, request: HttpRequest, pk, *args, **kwargs):
        if pk == 'self':
            return super().retrieve(request, pk, args, kwargs)
        raise PermissionDenied(
            "This endpoint can only be reached at /user/self/")

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    http_method_names = ['get', 'post', 'delete', 'head']

    def retrieve(self, request: HttpRequest, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request: HttpRequest, *args, **kwargs):
        start = request.data['start']
        end = request.data['end']
        room_uid = request.data['room']
        room = Room.objects.get(uid=room_uid)
        if room.is_available(start_date=start, end_date=end):
            with transaction.atomic():
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save(room=room)
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
