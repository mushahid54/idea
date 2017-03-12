from django.shortcuts import get_list_or_404
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from tracking.models import LiveSolarPowerData, ReferenceSolarPowerData
from tracking.serializers import LiveSolarPowerDataSerializer


class LivePowerConsumption(generics.CreateAPIView):
    # permission_classes = [permissions.IsAdminUser, ]
    # authentication_classes = [OAuth2Authentication, ]
    queryset = LiveSolarPowerData.objects.all()
    serializer_class = LiveSolarPowerDataSerializer


class PowerDataAnalysis(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAdminUser, ]
    # authentication_classes = [OAuth2Authentication, ]
    queryset = LiveSolarPowerData.objects.all()
    lookup_field = 'solar_system'
    lookup_url_kwarg = 'solar_system'
    serializer_class = None

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {"solar_system__solar_system_id": self.kwargs[lookup_url_kwarg]}
        obj = get_list_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve low_power data  based on the reference data
        :param request: data as input params
        :param args:
        :param kwargs: key value pair to get the system reference_id
        :return: list of dict with relevance data
        """
        live_solar_power_data = self.get_object()

        day, month, year = self.request.query_params.get('date', None).split('-')
        reference_data = ReferenceSolarPowerData.objects.filter(day=int(day), month=int(month),
                                                                solar_system__solar_system_id=self.kwargs['solar_system']).values('hour', 'power')

        power_stats_list = list()
        calculate_percentage_number = 0.80
        for item in reference_data:
            for obj in live_solar_power_data:
                if item['hour'] == obj.hour:
                    expected_power = item['power'] * calculate_percentage_number
                    if obj.power < expected_power:
                        power_stats_list.append({"live_power_dc": obj.power, "reference_power_dc": item['power'],
                                                 "hour": obj.hour, "reference_hour": item['hour']})

        return Response(power_stats_list, status=status.HTTP_200_OK)






