from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['POST'])
def Category_Add(request):
    serializer = Category_Serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else :
        return Response("data is not valid")
    return Response(serializer.data)

@api_view(['GET'])
def ViewCategory(request):
    data = FoodCategory.objects.all()
    serializer = Category_Serializer(data, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewFoodMenu(request):
    data = FoodMenu.objects.all()
    serializer = FoodMenuSerializer(data,many=True)
    return Response(serializer.data)
