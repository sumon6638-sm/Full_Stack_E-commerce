from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

from .models import Vehicle, Category
from .serializer import VehicleSerializer, VehicleFashionSerializer, CategorySerializer
from django.db.models import Q

class LatestVehicleList(APIView):
  def get(self, request, format=None):
    vehicles = Vehicle.objects.all()[0:6] # backend er url ee koyta kore object dekhabe seta ekhan theke control kora jabe...
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)

class VehicleDetail(APIView):
  def get_object(self, category_slug, vehicle_slug, vehicle_url):
    try:
      return Vehicle.objects.filter(category__slug=category_slug).get(url=vehicle_url)
    except Vehicle.DoesNotExist:
      raise Http404
  
  def get(self, request, category_slug, vehicle_slug, vehicle_url, format=None):
    vehicle = self.get_object(category_slug, vehicle_slug, vehicle_url)
    serializer = VehicleSerializer(vehicle)
    return Response(serializer.data)

class VehicleFashion(APIView):
  def get_object(self, category_slug, vehicle_slug):
    try:
      return Vehicle.objects.filter(category__slug=category_slug).get(slug=vehicle_slug)
    except Vehicle.DoesNotExist:
      raise Http404
  
  def get(self, request, category_slug, vehicle_slug, format=None):
    vehicleFashion = self.get_object(category_slug, vehicle_slug)
    serializer = VehicleFashionSerializer(vehicleFashion)
    return Response(serializer.data)

class CategoryDetail(APIView):
  def get_object(self, category_slug):
    try:
      return Category.objects.get(slug=category_slug)
    except Vehicle.DoesNotExist:
      raise Http404
  
  def get(self, request, category_slug, format=None):
    category = self.get_object(category_slug)
    serializer = CategorySerializer(category)
    return Response(serializer.data)