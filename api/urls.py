from django.urls import path
from . import views
from .routers import router

app_name = 'api'

urlpatterns = [
    path('', view=views.getRoutes),
    path('check/', view=views.checkAvailableRooms),
    path('overview/', view=views.overview)
]

urlpatterns += router.urls