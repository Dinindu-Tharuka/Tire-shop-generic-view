from django.urls import path, include

urlpatterns = [
    path('', include('api.customer.urls')),
    path('', include('api.services.urls')),
    path('', include('api.stock.urls')),
    path('', include('api.inventory.urls')),
    path('', include('api.billing.urls')),
    path('', include('api.user.urls')),
    path('', include('api.dag_section.urls')),
    path('', include('api.report.urls')),
]