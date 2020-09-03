import jwt
from django.contrib.auth import user_logged_in
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_payload_handler

from shop import settings
from .models import Category, UserAccount
from .serializers import CategoryListSerializer, UserSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by('position')
    serializer_class = CategoryListSerializer


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        phone_number = request.data['phone_number']

        user = UserAccount.objects.get(phone_number=phone_number)
        if user:
            try:
                payload = jwt_payload_handler(user.phone_number)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {'phone_number': user.phone_number, 'token': token, 'full_name': user.full_name}
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a phone and a full name'}
        return Response(res)
