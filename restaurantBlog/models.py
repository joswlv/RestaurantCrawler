from django.db import models

class RestaurantList(models.Model):
    restaurantName = models.CharField(max_length=200)
    restaurantAddress = models.CharField(max_length=300,blank=True,null=True)
    mangoRatingValue = models.FloatField(blank=True,null=True)
