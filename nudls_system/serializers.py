from rest_framework import serializers

from .models import Dragon, DragonFed, DragonLocation, Zone

class DragonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragon
        fields = '__all__'



class DragonFedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DragonFed
        fields = '__all__'

class DragonLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DragonLocation
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'maintainence_time']