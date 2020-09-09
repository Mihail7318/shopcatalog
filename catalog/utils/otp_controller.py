from datetime import datetime

from requests import Response


class Otp:
    def __init__(self, model_class):
        self.model_class = model_class

    def validatePhoneSendOtp(self, phone_number):
        if phone_number:
            phone = str(phone_number)
            user = self.model_class.objects.filter(phone_number=phone)

            if user.exists():
                key = send_otp(phone)
                user = user.first()
                user.creation_otp_time = datetime.datetime.now()
                user.otp = key
                user.save()
                if key:
                    return Response({
                        'status': True,
                        'detail': 'OTP sent successfully.'
                    })
                else:
                    return Response({
                        'status': False,
                        'detail': 'Sending OTP error.'
                    })

            else:
                key = send_otp(phone)
                if key:
                    self.model_class.objects.create(
                        phone_number=phone,
                        otp=key,
                        creation_otp_time=datetime.datetime.now()
                    )
                    return Response({
                        'status': True,
                        'detail': 'OTP sent successfully.'
                    })
                else:
                    return Response({
                        'status': False,
                        'detail': 'Sending OTP error.'
                    })
        else:
            return Response({

                'status': False,
                'detail': 'Phone number is not given in post request.'
            })

    def validateOtp(self, phone_number, otp_sent):
        if phone_number and otp_sent:
            user = self.model_class.objects.filter(phone_number=phone_number)
            if user.exists():
                user = user.first()
                otp = user.otp
                if str(otp_sent) == str(otp):
                    user.validated = True
                    user.otp = None
                    user.save()
                    return Response({
                        'status': True,
                        'detail': 'OTP matched.'
                    })

                else:
                    return Response({
                        'status': False,
                        'detail': 'OTP incorrect.'
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'User not exist.'
                })
        else:
            return Response({
                'status': False,
                'detail': 'Please provide both phone and otp for validations. '
            })
