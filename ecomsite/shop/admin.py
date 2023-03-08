from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-commerce Site"
admin.site.site_title = " ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

admin.site.register(Products)
admin.site.register(Order)