from rest_framework.routers import DefaultRouter
from monitor.api.views import MonitorViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'', MonitorViewSet, basename='monitor')
urlpatterns = router.urls
