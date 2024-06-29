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


class ReviewSerializer(serializers.Serializer):
    content = serializers.CharField()

    def create(self, validated_data):
        return super().create(validated_data)
    

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return super().create(validated_data)
    
class ProductsSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    review = serializers.CharField()
    category = serializers.CharField()

    def create(self, validated_data):
        return super().create(validated_data)