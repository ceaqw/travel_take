from django.http import JsonResponse
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import CityInfoSerializer
# Create your views here.


class CityInfo(GenericAPIView):

    serializer_class = CityInfoSerializer

    def get(self, request, *args, **kwargs):
        """
        Comeback a city info with json string.
        :return:
            {
                'id': 1,
                'city_name': 'xxx',
                'head_img_url': 'http:xxx'
            }
        """
        return JsonResponse({
            'id': 1,
            'city_name': 'xxx',
            'head_img_url': 'http:xxx'
        })

    def post(self, request, *args, **kwargs):
        return JsonResponse({'status': 'ok'})

