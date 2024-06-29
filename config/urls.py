from django.contrib import admin
from django.urls import path
from users.views import (TravelUpdateDestroyAPIView,HotelUpdateDestroyAPIView,KlassUpdateDestroyAPIView,
                         TravelAPIView,HotelAPIView,KlassAPIView, ProductCreateAPIView, ProductUpdateAPIView, ReviewCreateAPIView, ReviewUpdateAPIView, 
                              CategoryCreateAPIView, CategoryUpdateAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/nevs/<int:pk>/',TravelUpdateDestroyAPIView.as_view()),
    path('api/v1/nevs/',TravelAPIView.as_view()),
    path('api/v1/nevs/',HotelAPIView.as_view()),
    path('api/v1/nevs/',KlassAPIView.as_view()),
    path('api/v2/nevs/<int:pk>/',HotelUpdateDestroyAPIView.as_view()),
    path('api/v2/nevs/',HotelUpdateDestroyAPIView.as_view()),
    path('api/v3/nevs/<int:pk>/',KlassUpdateDestroyAPIView.as_view()),
    path('api/v3/nevs/',KlassUpdateDestroyAPIView.as_view()),
    path('api/v1/products/create/', ProductCreateAPIView.as_view()),
    path('api/v1/products/update/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('api/v1/review/create/', ReviewCreateAPIView.as_view()),
    path('api/v1/review/update/<int:pk>/', ReviewUpdateAPIView.as_view()),
    path('api/v1/category/create/', CategoryCreateAPIView.as_view()),
    path('api/v1/category/update/<int:pk>/', CategoryUpdateAPIView.as_view()),
]
