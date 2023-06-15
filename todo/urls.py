from django.urls import include, path
from rest_framework import routers
from .views import TODOViewSet

router = routers.DefaultRouter()
router.register('todos',TODOViewSet)

urlpatterns = [
    path('',include(router.urls))
]
