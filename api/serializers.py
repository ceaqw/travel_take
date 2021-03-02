from abc import ABC

from rest_framework import serializers
from .models import *


class CityInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityInfo
        fields = ('id', 'city_name', 'head_img_url')
        extra_kwargs = {
            'id': {
                'required': False,
                "help_text": "Auto-create city id with system."
            },
            'city_name': {
                "help_text": "ity name, max length with 50 charset.",
                "max_length": 50
            },
            'head_img_url': {
                'required': False,
                "help_text": "Auto-create city main-img href with system, need submit the img file by you!"
            },
        }


class MomentInfoSerializer(serializers.ListSerializer, ABC):

    class Meta:
        model = MomentInfo
        fields = '__all__'
