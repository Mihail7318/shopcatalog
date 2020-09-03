from django.contrib import admin

from .models import Category, Attribute, Value, Product, UserAccount

admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Value)
admin.site.register(Product)
admin.site.register(UserAccount)
