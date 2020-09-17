from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist

from catalog.models import UserAccount


class JWTBackend(BaseBackend):

    def authenticate(self, request, phone_number=None):
        try:
            user = UserAccount.objects.get(phone_number=phone_number)

        except ObjectDoesNotExist:
            user = UserAccount(phone_number=phone_number)
            user.is_active = True
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return UserAccount.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
