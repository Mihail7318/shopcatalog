from django.contrib.auth.models import BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.brand


class CustomManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, full_name=None):
        user = self.model(phone_number=phone_number, full_name=full_name)
        user.save()
        return user

    def create_user(self, phone_number, full_name=None):
        return self._create_user(phone_number, full_name)

    def create_superuser(self, phone_number, full_name=None):
        return self._create_user(phone_number, full_name)


class UserAccount(models.Model):
    phone_number = PhoneNumberField(unique=True, null=False)
    full_name = models.CharField(name="full_name", null=True, max_length=60, help_text="ФИО")
    otp = models.CharField(max_length=4, blank=True, null=True)
    creation_otp_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, unique=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
