import jwt
from django.conf import settings
from rest_framework import (exceptions)
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response

from catalog.models import UserAccount
from catalog.utils.jwt.token_util import generate_access_token
from shop import settings


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
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


def refresh_access_token_view(refresh_token):
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided.')
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'expired refresh token, please login again.')

    user = UserAccount.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')

    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')

    access_token = generate_access_token(user)

    return Response({'access_token': access_token})
