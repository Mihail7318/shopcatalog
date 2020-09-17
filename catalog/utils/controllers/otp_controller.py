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
            UserAccount.objects.create(phone_number=phone_number, otp=key, creation_otp_time=datetime.now())
            return {'status': status.HTTP_200_OK,
                    'detail': 'OTP sent successfully.'}

        user.creation_otp_time = datetime.now()
        user.otp = key
        user.save()
        return {'status': status.HTTP_200_OK,
                'detail': 'OTP sent successfully.'}

    @classmethod
    def validate_otp(cls, phone_number, otp_sent):
        print("validate otp ! WORKKK")

        if not (phone_number and otp_sent):
            return {'status': status.HTTP_400_BAD_REQUEST,
                    'detail': 'Please provide both phone and otp for validations.'}

        user = UserAccount.objects.filter(phone_number=phone_number).first()

        if not user:
            return {'status': status.HTTP_400_BAD_REQUEST,
                    'detail': 'User not exist.'}

        otp = user.otp
        otp_lifetime = datetime.now() - user.creation_otp_time.replace(tzinfo=None)
        if otp_sent == otp and otp_lifetime < timedelta(seconds=30):
            user.validated = True
            user.otp = None
            user.creation_otp_time = None
            user.save()
            return {'status': status.HTTP_200_OK,
                    'detail': 'OTP matched.'}

        else:
            return {'status': status.HTTP_400_BAD_REQUEST,
                    'detail': 'OTP incorrect or lifetime is end.'}
