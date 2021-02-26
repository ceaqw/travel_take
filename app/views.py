from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import TmpSerializer


class IndexView(TemplateView, generics.GenericAPIView):
    """
    get:
    Response the main page. It's need <b>FLL</b> completed!
        <b style="color:red;">Action:</b> submit location: ~/app/templates/index.html
    """
    serializer_class = TmpSerializer
    template_name = "index.html"
    # extra_context = {
    #     'name': 'cc',
    # }


class MomentsView(TemplateView, generics.GenericAPIView):
    """
    get:
    Response the moment page. It's need <b>FLL</b> completed!
        <b style="color:red;">Action:</b> submit location: ~/app/templates/moment.html
    """
    serializer_class = TmpSerializer
    template_name = "moment.html"
