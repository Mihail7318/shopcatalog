from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    position = models.IntegerField(name="position", verbose_name="Позиция")

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(name="name", max_length=40)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Value(models.Model):
    value = models.CharField(name="value", max_length=40)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="values")

    def __str__(self):
        return self.value

    


class Product(models.Model):
    name = models.CharField(name="name", max_length=40)
    brand = models.CharField(name="brand", max_length=40)
    price = models.IntegerField(name="price", default=0)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.ManyToManyField(Value)
