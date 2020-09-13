from django.urls import path

from .views import CreateUserAPIView, ValidatePhoneSendOTP, ValidateOTP

urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('validatePhone', ValidatePhoneSendOTP.as_view(), name="validate_phone_send_otp"),
    path('validateOtp', ValidateOTP.as_view(), name="validate_otp"),

    path('category/', views.CategoryListView.as_view()),
    path('category/<int:idcat>/attr', views.AtributeView.as_view()),
    path('category/<int:pk>/products', views.ProductView.as_view()),
]
app_name = 'catalog'
