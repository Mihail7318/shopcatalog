from django.urls import path

from .views import CreateUserAPIView, ValidatePhoneSendOTP, ValidateOTP

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('validatePhone', ValidatePhoneSendOTP.as_view(), name="validate_phone_send_otp"),
    path('validateOtp', ValidateOTP.as_view(), name="validate_otp"),
]
app_name = 'catalog'
