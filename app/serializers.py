from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Test
        fields = ('id', 'name', 'age')
        extra_kwargs = {
            'name': {
                'help_text': 'This is a string filed!',
                'min_length': 6,
                'max_length': 12,
                'error_messages': {
                    'min_length': '6个字符',
                    'max_length': '12个字符',
                },
            },
            'age': {
                'help_text': '密码６－８位',
            }
        }
