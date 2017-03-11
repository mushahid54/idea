from django.contrib import admin
from tracking.models import SolarSystem, LiveSolarPowerData, ReferenceSolarPowerData


class SolarSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'solar_system_id', 'latitude',  'longitude', 'city')

admin.site.register(SolarSystem, SolarSystemAdmin)


class LiveSolarPowerDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'month', 'day', 'get_city',  'power')

admin.site.register(LiveSolarPowerData, LiveSolarPowerDataAdmin)


class ReferenceSolarPowerDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'month', 'day', 'hour', 'get_city', 'solar_system', 'power')

admin.site.register(ReferenceSolarPowerData, ReferenceSolarPowerDataAdmin)