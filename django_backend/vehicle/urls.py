from django.urls import path, include

from vehicle import views

urlpatterns = [
    path('latest-vehicles/', views.LatestVehicleList.as_view()),
    path('<slug:category_slug>/<slug:vehicle_slug>/<slug:vehicle_url>/', views.VehicleDetail.as_view()),
    path('<slug:category_slug>/<slug:vehicle_slug>/', views.VehicleFashion.as_view()),
    path('<slug:category_slug>/', views.CategoryDetail.as_view()),
]
