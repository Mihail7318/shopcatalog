from django.contrib.auth.backends import BaseBackend
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from catalog.models import UserAccount
from catalog.utils.controllers.otp_controller import OtpController


class JWTBackend(BaseBackend):

    def authenticate(self, request, phone_number=None, otp_sent=None):
        if OtpController.validate_otp(phone_number, otp_sent)['status'] == status.HTTP_400_BAD_REQUEST:
            return None
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
