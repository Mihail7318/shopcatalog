from django.urls import path

from .views import CreateUserAPIView, ValidatePhoneSendOTP, ValidateOTPLogin, profile, refresh_obtain_tokens

urlpatterns = [

    path('create', CreateUserAPIView.as_view()),
    path('validatePhone', ValidatePhoneSendOTP.as_view(), name="validate_phone_send_otp"),
    path('validateCode', ValidateOTPLogin.as_view(), name="val"),
    path('profile', profile, name="profile"),
    path('refresh', refresh_obtain_tokens),
]
app_name = 'catalog'
