# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	user_id=models.AutoField(primary_key=True,default=0)
	name=models.CharField(max_length=200)
	contact_no=models.CharField(max_length=10)
	wallet=models.IntegerField(default=0)
	password=models.CharField(max_length=200,default="")
	email_id=models.CharField(max_length=200,default="")
class Order(models.Model):
	order_id=models.AutoField(primary_key=True)
	total_amount=models.IntegerField()
	delivery_address=models.CharField(max_length=200)
	order_date=models.DateTimeField()
	delivery_date=models.DateTimeField()
	delivery_status=models.CharField(max_length=10)
	return_status=models.CharField(max_length=200)
	mobile_number=models.CharField(max_length=10)
class Cart(models.Model):
	cart_id=models.AutoField(primary_key=True)
	cart_amount=models.IntegerField()
class Feedback(models.Model):
	feedback_id=models.AutoField(primary_key=True)
	content=models.CharField(max_length=1000)
	approval=models.CharField(max_length=200)
	upvotes=models.IntegerField()
class Shipper(models.Model):
	shipper_id=models.AutoField(primary_key=True)
	delivery_charges=models.IntegerField()
	location=models.CharField(max_length=200)
class Payment(models.Model):
	payment_id=models.AutoField(primary_key=True)
	pay_amount=models.IntegerField()
	pay_date=models.DateTimeField()
	status=models.CharField(max_length=200)
class Bank_Detail(models.Model):
	card_no=models.CharField(max_length=16)
	bank_name=models.CharField(max_length=200)
	data_on_card=models.CharField(max_length=200)
	card_type=models.CharField(max_length=10)
class Chocolate(models.Model):
	chocolate_id=models.AutoField(primary_key=True)
	price=models.IntegerField()
	name=models.CharField(max_length=200)
	quantity_available=models.IntegerField()
	ingredients=models.CharField(max_length=1000)
	ratings=models.IntegerField()
	quantities_sold=models.IntegerField()
	description=models.CharField(max_length=200)