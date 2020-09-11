from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('category/<int:idcat>', views.AtributeView.as_view()),
]
