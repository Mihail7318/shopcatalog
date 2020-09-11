from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('category/<int:idcat>/attr', views.AtributeView.as_view()),
    path('category/<int:pk>/products', views.ProductView.as_view()),
]
