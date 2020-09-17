from django.contrib.auth.backends import BaseBackend

from catalog.models import UserAccount


class JWTBackend(BaseBackend):

    def authenticate(self, request, phone_number=None):
        try:
            user = UserAccount.objects.get(phone_number=phone_number)
        except UserAccount.DoesNotExist:
            user = UserAccount(phone_number=phone_number)
            user.save()
        return user

    def get_user(self, phone_number):
        try:
            return UserAccount.objects.get(phone_number=phone_number)
        except UserAccount.DoesNotExist:
            return None
