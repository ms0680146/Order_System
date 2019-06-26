from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('piechart/', views.piechart, name='piechart'),
    path('cohort/', views.cohort, name='cohort'),
    path('barchart/', views.barchart, name='barchart'),
    path('api/shipping/data/', views.get_shipping_data, name='api-shipping-data'),
    path('api/top3/products/', views.get_top3_products, name='api-top3-products'),
]