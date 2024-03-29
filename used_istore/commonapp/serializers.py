from rest_framework import serializers
from .models import *

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = '__all__'
        
# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CityModel
#         fields = '__all__'
        
# class ColorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ColorModel
#         fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionModel
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields ='__all__'

class ModelnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelnameModel
        fields ='__all__'
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # condition = serializers.SerializerMethodField()
    images = ImageSerializer(many=True)
    class Meta:
        model = ProductModel
        fields = '__all__'

    # def get_condition(self,obj):
    #     if obj.condition:
    #         v_obj = ConditionModel.objects.filter(id=obj.condition.id).select_related('condition')
    #         v_qs = ConditionSerializer(v_obj,many=True)
    #         return v_qs.data
    #     else:pass
class ProductfullSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['model_name','title','buyprice','buystatus','created_date','id']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestimonialModel
        fields = '__all__'