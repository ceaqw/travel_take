# from django.shortcuts import render
# from django.views import View
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .serializers import UserSerializer
from rest_framework import generics
# Create your views here.


class TestView(generics.GenericAPIView):
    """
    get:
    返回所有图书信息.

    post:
    新建图书.
    """
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is a test response!")

    def post(self, request,  *args, **kwargs):
        return JsonResponse({'name': 'test', 'age': 18})