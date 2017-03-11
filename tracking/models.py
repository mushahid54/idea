from django.db import models

# Create your models here.


class SolarSystem(models.Model):
    solar_system_id = models.CharField(max_length=50, unique=True)
    capacity = models.FloatField()
    city = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.solar_system_id


class ReferenceSolarPowerData(models.Model):
    """
     Why not used datetime: Data is not year specific.
    """

    solar_system = models.ForeignKey(SolarSystem, on_delete=models.PROTECT)
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()   # Assuming each  hour like 1: AM , 2:Am
    power = models.FloatField()

    def __str__(self):
        return self.solar_system.solar_system_id

    def get_solar_panel_latitude(self):
        if self.solar_system:
            return self.solar_system.latitude
        else:
            pass

    def get_solar_panel_longitude(self):
        if self.solar_system:
            return self.solar_system.longitude
        else:
            pass

    def get_city(self):
        if self.solar_system:
            return self.solar_system.city
        else:
            return "N/A"

class LiveSolarPowerData(models.Model):
    """
        Why not used datetime: Data is not year specific.
    """

    solar_system = models.ForeignKey(SolarSystem, on_delete=models.PROTECT)
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()   # Assuming each  hour like 1: AM , 2:Am
    power = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return self.solar_system.solar_system_id

    def get_solar_panel_latitude(self):
        if self.solar_system:
            return self.solar_system.latitude
        else:
            pass

    def get_solar_panel_longitude(self):
        if self.solar_system:
            return self.solar_system.longitude
        else:
            pass

    def get_city(self):
        if self.solar_system:
            return self.solar_system.city
        else:
            return "N/A"

