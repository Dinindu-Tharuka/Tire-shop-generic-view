from django.urls import path
from . import views

urlpatterns =[
    path('logout/', views.LogOutView.as_view(), name='logout')
]