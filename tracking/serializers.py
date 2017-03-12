from rest_framework import serializers
from tracking.models import LiveSolarPowerData, SolarSystem



class LiveSolarPowerDataSerializer(serializers.ModelSerializer):
    solar_system = serializers.SlugRelatedField(slug_field='solar_system_id', queryset=SolarSystem.objects.all())
    timestamp = serializers.DateTimeField(write_only=True)

    class Meta:
        model = LiveSolarPowerData
        fields = ('month', 'day', 'hour', 'power','year', 'solar_system', 'timestamp')
        extra_kwargs = {
                        'month': {
                            "read_only": True},
                        'day': {
                            "read_only": True},
                        'hour': {
                            "read_only": True},
                        'year': {
                            "read_only": True}}


    def create(self, validated_data):
        # year, month, day, hour = self._get_date(validated_data['timestamp'])
        month = validated_data['timestamp'].month
        day = validated_data['timestamp'].day
        year = validated_data['timestamp'].year
        hour = validated_data['timestamp'].hour
        validated_data.pop('timestamp')

        return LiveSolarPowerData.objects.create(month=month, day=day, year=year, hour=hour, **validated_data)




