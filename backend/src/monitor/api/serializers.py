from rest_framework import serializers
from monitor.models import Monitor


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = ('date', 'kw',
                  'time', 'voltage', 'current')
