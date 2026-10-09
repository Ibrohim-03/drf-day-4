from django.urls import path
from .views import *
urlpatterns = [
    path('product',product),
    path('category',category),
    path('review',review),
    path('user',user),
    path('product/<int:id>',product_det)
]
