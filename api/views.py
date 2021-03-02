from django.http import JsonResponse
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from .serializers import CityInfoSerializer, MomentInfoSerializer
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


class MomentList(ListAPIView):
    """
    get:
    Response is moment_list like:
        [<br>
            {moment_id:'xxx', user:'xxx', is_liked:false, liked_num:123, user_head:'http://xxx', content:'xxx', img:'http://xxx'},<br>
            {moment_id:'xxx', user:'xxx', is_liked:false, liked_num:123, user_head:'http://xxx', content:'xxx', img:'http://xxx'}<br>
        ]
    """
    serializer_class = MomentInfoSerializer
