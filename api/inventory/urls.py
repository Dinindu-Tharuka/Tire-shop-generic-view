from django.urls import path
from . import views

urlpatterns = [
    path('item-categories/', views.ItemCategoryList.as_view()),
    path('item-categories/<str:pk>/', views.ItemCategoryDetail.as_view()),
    path('suppliers/', views.SupplierList.as_view()),
    path('suppliers-all/', views.SupplierAllList.as_view()),
    path('suppliers/<str:pk>/', views.SupplierDetail.as_view()),
    path('items-pagination/', views.ItemListPagination.as_view()),
    path('items/', views.ItemList.as_view()),
    path('items/<str:pk>/', views.ItemDetail.as_view()),

]
