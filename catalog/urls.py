from django.urls import path

from .views import CreateUserAPIView, ValidatePhoneSendOTP, ValidateOTPLogin, profile

urlpatterns = [

    path('create', CreateUserAPIView.as_view()),
    path('validatePhone', ValidatePhoneSendOTP.as_view(), name="validate_phone_send_otp"),
    path('validateCode', ValidateOTPLogin.as_view(), name="val"),
    path('profile', profile, name="profile"),
]
app_name = 'catalog'
