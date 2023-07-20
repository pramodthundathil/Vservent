from django.contrib import admin
from .models import *


admin.site.register(FoodCategory)
admin.site.register(FoodMenu)
admin.site.register(FoodOrder)
admin.site.register(BillOrder)
admin.site.register(Tables)