# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=200)
	contact_no=models.CharField(max_length=10)