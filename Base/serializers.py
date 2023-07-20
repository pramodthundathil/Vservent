from rest_framework.serializers import ModelSerializer, ImageField
from .models import FoodCategory, FoodMenu


class Category_Serializer(ModelSerializer):
    category_image = ImageField(max_length=None, use_url=True)
    class Meta:
        model = FoodCategory
        fields = "__all__"
        
class FoodMenuSerializer(ModelSerializer):
    food_image = ImageField(max_length=None, use_url=True)
    class Meta:
        model = FoodMenu
        fields = "__all__"