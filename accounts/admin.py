from django.contrib import admin
from . models import *

# Register your models here.

MyModels = [Customer, Order, Product, Tag]
admin.site.register(MyModels)