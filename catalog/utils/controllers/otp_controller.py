import random
from datetime import datetime, timedelta

from rest_framework import status

from catalog.models import UserAccount


class OtpController:

    @staticmethod
    def _send_otp(phone_number):
        key = str(random.randint(999, 9999))
        print("\n{0} digital code is {1}.\n".format(phone_number, key))
        # free sms api
        return key

    @classmethod
    def validate_phone_send_otp(cls, phone_number):
        if not phone_number:
            return {'status': status.HTTP_400_BAD_REQUEST,
                    'detail': 'Phone number is not given in post request.'}

        user = UserAccount.objects.filter(phone_number=phone_number).first()
        key = cls._send_otp(phone_number)

        if not user:
            UserAccount.objects.create(phone_number=phone_number, otp=key, creation_otp_time=datetime.now(),
                                       is_active=True)
            return {'status': status.HTTP_200_OK,
                    'detail': 'OTP sent successfully.'}

        user.creation_otp_time = datetime.now()
        user.otp = key
        user.is_active = True
        user.save()
        return {'status': status.HTTP_200_OK,
                'detail': 'OTP sent successfully.'}

    @classmethod
    def validate_otp(cls, phone_number, otp_sent):

        if not (phone_number and otp_sent):
            return {'status': status.HTTP_400_BAD_REQUEST,
                    'detail': 'Please provide both phone and otp for validations.'}

        user = UserAccount.objects.filter(phone_number=phone_number).first()
        otp_lifetime = datetime.now() - user.creation_otp_time.replace(tzinfo=None)

        if not otp_sent == user.otp and otp_lifetime < timedelta(seconds=60):
            return {'status': status.HTTP_400_BAD_REQUEST,
                    'detail': 'OTP incorrect or lifetime is end.'}

        user.otp = None
        user.is_active = True
        user.save()
        return {'status': status.HTTP_200_OK,
                'detail': 'OTP matched.'}
