from rest_framework import generics
from tracking.models import LiveSolarPowerData
from tracking.serializers import LiveSolarPowerDataSerializer


class LivePowerConsumption(generics.CreateAPIView):
    # permission_classes = [permissions.IsAdminUser, ]
    # authentication_classes = [OAuth2Authentication, ]
    queryset = LiveSolarPowerData.objects.all()
    serializer_class = LiveSolarPowerDataSerializer
