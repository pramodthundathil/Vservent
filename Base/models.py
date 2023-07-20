from django.db import models

class Tables(models.Model):
    table_number  = models.IntegerField()
    nubmber_of_seats = models.IntegerField()
    table_location = models.CharField(max_length=1000,null=True,blank=True)
    
    def __str__(self):
        return self.table_number
    

class FoodCategory(models.Model):
    foodcategory_name = models.CharField(max_length=255)
    category_image = models.FileField(upload_to='category_image')
    diat = models.BooleanField(default=True)
    added_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.foodcategory_name

class FoodMenu(models.Model):
    foodname = models.CharField(max_length=255)
    food_description = models.CharField(max_length=1000)
    food_image = models.FileField(upload_to='food_image')
    food_category = models.ForeignKey(FoodCategory,on_delete=models.SET_NULL,null=True,blank=True)
    food_price  = models.FloatField()
    food_availablity = models.BooleanField(default=False)
    
    def __str__(self):
        return self.foodname
    
class FoodOrder(models.Model):
    food = models.ForeignKey(FoodMenu,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    table = models.ForeignKey(Tables,on_delete=models.CASCADE)
    order_time = models.TimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=255)
    
class BillOrder(models.Model):
    foodmenu = models.ManyToManyField(FoodMenu)
    total_price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    payment_mode = models.CharField(max_length=255,null=True)
    payment_ref = models.CharField(max_length=1000,null=True,blank=True)
    
    
    
