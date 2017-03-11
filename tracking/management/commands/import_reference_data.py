import datetime
from django.core.management import BaseCommand
import requests
from tracking.models import ReferenceSolarPowerData, SolarSystem


class Command(BaseCommand):
    help = "Import reference solar data from the Reference Data API endpoint and store in ReferenceDataModel"

    def handle(self, *args, **options):
        # create solar sytems
        SolarSystem.objects.get_or_create(
            solar_system_id="mum_000001", capacity=10.0, city='Mumbai', latitude=19.0, longitude=73.0
        )
        SolarSystem.objects.get_or_create(
            solar_system_id="bng_000001", capacity=5.0, city='Bangalore', latitude=13.0, longitude=78.0
        )

        SolarSystem.objects.get_or_create(
            solar_system_id="del_000001", capacity=3.0, city='Delhi', latitude=28.0, longitude=77.0
        )
        # populate reference data
        url = "https://developer.nrel.gov/api/pvwatts/v5.json"
        for system in SolarSystem.objects.all():
            self.stdout.write("Working on {0}...".format(system.city))
            params = {
                "api_key":"DEMO_KEY",
                "lat":int(system.latitude),
                "lon":int(system.longitude),
                "system_capacity": int(system.capacity),
                "azimuth": 180,
                "tilt": int(system.latitude),
                "array_type": 1,
                "module_type": 1,
                "losses": 10,
                "dataset": "IN",
                "timeframe": "hourly"
            }
            self.stdout.write("--> Fetching data from Endpoint...")
            response = requests.get(url=url, params=params)

            if response.status_code == 200:

                self.stdout.write("--> Writing in database...")
                data = response.json()['outputs']['dc']
                hours_in_a_day = 24

                for loop_counter, power_reading in enumerate(data):
                    # import pdb; pdb.set_trace()
                    hour = loop_counter % hours_in_a_day
                    day_of_year = int(loop_counter / hours_in_a_day) + 1
                    month = self.__get_month(day_of_year)
                    day_of_month = self.__get_day_of_month(day_of_year, month)
                    ReferenceSolarPowerData.objects.create(day=day_of_month, month=month, power=power_reading, hour=hour,
                                                           solar_system=system)

                self.stdout.write("--> Done...")

    @staticmethod
    def __get_month(day_number):
        # import pdb; pdb.set_trace()
        month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        cumulative_month_days = 0
        month = 1
        for month_number, month_days in enumerate(month_days_list, 1):
            cumulative_month_days += month_days

            if day_number > cumulative_month_days:
                continue
            else:
                month = month_number
                break

        return month

    @staticmethod
    def __get_day_of_month(day_of_year, month):
        return (datetime.datetime(2001, 1, 1) + datetime.timedelta(day_of_year - 1)).day




















