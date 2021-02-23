from django.db import models
import datetime
from django.contrib.auth.models import User


class WeekMenu(models.Model):
	restaurant = models.CharField(max_length=50)
	menu_name = models.CharField(max_length=50)

	monday = models.CharField(max_length=500)
	monday_calories = models.FloatField()
	tuesday = models.CharField(max_length=500)
	tuesday_calories = models.FloatField()
	wednesday = models.CharField(max_length=500)
	wednesday_calories = models.FloatField()
	thursday = models.CharField(max_length=500)
	thursday_calories = models.FloatField()
	friday = models.CharField(max_length=500)
	friday_calories = models.FloatField()
	saturday = models.CharField(max_length=500)
	saturday_calories = models.FloatField()
	sunday = models.CharField(max_length=500)
	sunday_calories = models.FloatField()

	begin_date = models.DateField(default=datetime.date.today)


class Restaurant(models.Model):
	user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	cellphone = models.CharField(max_length=50)
	fb_link = models.CharField(max_length=50)

	class Meta:
		permissions = (
            ("verified_restaurant", "Verified restaurant account"),
        )
	
