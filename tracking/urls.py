from django.conf.urls import url
from tracking.views import LivePowerConsumption, PowerDataAnalysis

urlpatterns = [
    url(r'solar_power_track/$', LivePowerConsumption.as_view(), name='live_power_consumption_to_compare'),
    url(r'solar_system/(?P<solar_system>\w+)/power_inspection/', PowerDataAnalysis.as_view(), name="live_power_data_analysis")

]

