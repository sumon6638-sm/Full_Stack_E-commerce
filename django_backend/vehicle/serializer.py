from pyexpat import model
from rest_framework import serializers

from .models import Category, Vehicle

class VehicleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vehicle
    fields = (
      "id",
      "name",
      "get_absolute_url",
      "description",
      "price",
      "get_image",
      "get_thumbnail"
    )

class CategoryFashionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = (
      "id",
      "name",
      "get_absolute_url",
      "slug",
      "vehicles"
    )

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = (
      "id",
      "name",
      "get_absolute_url",
      "vehicles"
    )