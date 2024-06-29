from rest_framework import serializers

from .models import Hotel,Travel,Klass

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'