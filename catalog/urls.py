from django.urls import path

from .views import CreateUserAPIView, ValidatePhoneSendOTP, Val, get_user_id, out

urlpatterns = [

    path('create', CreateUserAPIView.as_view()),
    path('validatePhone', ValidatePhoneSendOTP.as_view(), name="validate_phone_send_otp"),
    path('JWTAuth', Val.as_view(), name="val"),
    path('testuser', get_user_id),
    path('out', out),
    # path('category/', views.CategoryListView.as_view()),
    # path('category/<int:idcat>/attr', views.AtributeView.as_view()),
    # path('category/<int:pk>/products', views.ProductView.as_view()),
]
app_name = 'catalog'
