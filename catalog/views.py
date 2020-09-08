import random
from django.contrib.sites import requests
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, UserAccount
from .serializers import CategoryListSerializer, UserSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by('position')
    serializer_class = CategoryListSerializer


class CreateUserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        user = request.POST.dict()
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)  # Error
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ValidatePhoneSendOTP(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        if phone_number:
            phone = str(phone_number)
            user = UserAccount.objects.filter(phone_number=phone)

            if user.exists():
                key = send_otp(phone)
                if key:
                    return Response({
                        'status': False,
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
                    UserAccount.objects.create(
                        phone_number=phone,
                        otp=key,
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


def send_otp(phone):
    if phone:
        key = random.randint(999, 9999)
        print(key)
        return key
    else:
        return False


class ValidateOTP(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone_number', False)
        otp_sent = request.data.get('otp', False)

        if phone and otp_sent:
            user = UserAccount.objects.filter(phone_number=phone)
            if user.exists():
                user = user.first()
                otp = user.otp
                if str(otp_sent) == str(otp):
                    user.validated = True
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
                'detail': 'Please provide both phone and otp for validations'
            })
