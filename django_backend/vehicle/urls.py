from django.urls import path, include

from vehicle import views

urlpatterns = [
    path('latest-vehicles/', views.LatestVehicleList.as_view()),
    path('<slug:category_slug>/<slug:category_fashion>/<slug:vehicle_slug>/', views.VehicleDetail.as_view()),
]
