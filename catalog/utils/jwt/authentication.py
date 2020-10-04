import jwt
from django.conf import settings
from rest_framework import (exceptions)
from rest_framework.authentication import BaseAuthentication

from catalog.models import UserAccount
from shop import settings


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('X-Authorization')
        if not authorization_header:
            return None
        try:
            access_token = authorization_header
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired.')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = UserAccount.objects.filter(phone_number=payload['phone_number']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')

        return (user, None)
