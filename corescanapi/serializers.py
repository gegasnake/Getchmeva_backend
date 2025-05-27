from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'barcode',
            'url',
            'name',
            'generic_name',
            'quantity',
            'brands',
            'categories',
            'ingredients_text',
            'ingredients_analysis',
            'allergens',
            'traces',
            'serving_size',
            'serving_quantity',
            'no_nutrition_data',
            'additives',
            'nutriscore_score',
            'nutriscore_grade',
            'nova_group',
            'ecoscore_score',
            'ecoscore_grade',
            'unique_scans_n',
            'popularity_tags',
            'last_image_t',
            'last_image_datetime',
            'image_url',
            'image_small_url',
            'image_ingredients_url',
            'image_ingredients_small_url',
            'image_nutrition_url',
            'image_nutrition_small_url',
            'energy_100g',
            'fat_100g',
            'image',
            'is_vegan',
        ]
