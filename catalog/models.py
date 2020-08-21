from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    position = models.IntegerField(name="position")

    def __str__(self):
        return self.name


class Value(models.Model):
    value = models.CharField(max_length=40)

    def __str__(self):
        return self.value


class Attribute(models.Model):
    name = models.CharField(max_length=40)
    category = models.ManyToManyField(Category)
    value = models.ManyToManyField(Value)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
