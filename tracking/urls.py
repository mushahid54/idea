from django.conf.urls import url
from tracking.views import LivePowerConsumption

urlpatterns = [
    url(r'solar_power_track/$', LivePowerConsumption.as_view(), name='live_power_consumption_to_compare'),

]

