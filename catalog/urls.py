from django.urls import path

from .views import CreateUserAPIView, ValidatePhoneSendOTP, ValidateOTP

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('validatePhone', ValidatePhoneSendOTP.as_view()),
    path('validateOtp', ValidateOTP.as_view()),
]
app_name = 'catalog'
