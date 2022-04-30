from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

from .models import Vehicle
from .serializer import VehicleSerializer

class LatestVehicleList(APIView):
  def get(self, request, format=None):
    vehicles = Vehicle.objects.all()[0:6] # backend er url ee koyta kore object dekhabe seta ekhan theke control kora jabe...
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)

class VehicleDetail(APIView):
  def get_object(self, category_slug, category_fashion, vehicle_slug):
    try:
      return Vehicle.objects.filter(category__slug=category_slug).get(slug=vehicle_slug)
    except Vehicle.DoesNotExist:
      raise Http404
  
  def get(self, request, category_slug, category_fashion, vehicle_slug, format=None):
    vehicle = self.get_object(category_slug, category_fashion, vehicle_slug)
    serializer = VehicleSerializer(vehicle)
    return Response(serializer.data)