from django.shortcuts import render

# Create your views here.
from monitor.models import Monitor
from .serializers import MonitorSerializer
from rest_framework import viewsets


class MonitorViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MonitorSerializer
    queryset = Monitor.objects.all()
