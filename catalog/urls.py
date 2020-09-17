from django.urls import path

from .views import CreateUserAPIView, ValidatePhoneSendOTP, ValidateOTPLogin, out, testfunk

urlpatterns = [

    path('create', CreateUserAPIView.as_view()),
    path('validatePhone', ValidatePhoneSendOTP.as_view(), name="validate_phone_send_otp"),
    path('JWTAuth', ValidateOTPLogin.as_view(), name="val"),
    path('out', out),
    path('test', testfunk),
    # path('category/', views.CategoryListView.as_view()),
    # path('category/<int:idcat>/attr', views.AtributeView.as_view()),
    # path('category/<int:pk>/products', views.ProductView.as_view()),
]
app_name = 'catalog'
