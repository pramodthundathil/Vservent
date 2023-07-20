from django.urls import path 
from .import views 

urlpatterns = [
    path("Category_Add",views.Category_Add,name = 'Category_Add'),
    path("ViewCategory",views.ViewCategory,name="ViewCategory"),
    path("ViewFoodMenu",views.ViewFoodMenu,name="ViewFoodMenu"),
    
]
