from django.contrib import admin

from .models import Attribute, Category, Product, Value

admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Value)
admin.site.register(Product)

