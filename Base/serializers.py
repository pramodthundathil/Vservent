from rest_framework.serializers import ModelSerializer
from .models import FoodCategory, FoodMenu


class Category_Serializer(ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = "__all__"
        
class FoodMenuSerializer(ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = "__all__"