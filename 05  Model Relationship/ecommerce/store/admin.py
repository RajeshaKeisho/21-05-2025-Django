from django.contrib import admin

# Register your models here.
from .models import Customer, Address, Category, Product, Order

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
