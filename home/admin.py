# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User,Order,Cart,Feedback,Shipper,Payment,Bank_Detail,Chocolate

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Feedback)
admin.site.register(Shipper)
admin.site.register(Payment)
admin.site.register(Bank_Detail)
admin.site.register(Chocolate)

