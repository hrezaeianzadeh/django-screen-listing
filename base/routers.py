from rest_framework.routers import APIRootView, DefaultRouter
from .views import UserViewSet, ReservationViewSet


class Root(APIRootView):
    """Listing Basic APIs"""

class Router(DefaultRouter):
    APIRootView = Root    

router = Router()

# Register ViewSets from base app
router.register('user', UserViewSet, 'user')
router.register('reservation', ReservationViewSet, 'reservation')