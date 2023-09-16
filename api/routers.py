from rest_framework.routers import APIRootView, DefaultRouter
from base.routers import router as base_router


class ListingAPIRoot(APIRootView):
    """Root view for Listing APIs"""


class Router(DefaultRouter):
    APIRootView = ListingAPIRoot


router = Router()

router.registry.extend(base_router.registry)
