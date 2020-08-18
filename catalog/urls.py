from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('category/<int:id_cat>/attrs/', views.AttributeListView.as_view())
]