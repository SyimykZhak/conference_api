
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from .serializers import *

from rest_framework.response import Response

class ConferenceListView(generics.ListAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceListSerializers


class ConferenceDetailView(generics.RetrieveAPIView):
    queryset = Conference.objects.filter(draft=False)
    serializer_class = ConferenceDetailSerializer 
    lookup_field = 'url'


class RegisterCreateView(APIView):
    def post(self, request):
        register = CreateRegisterSerializer(data=request.data)
        if register.is_valid():
            register.save()
        return Response(status=201)

class WorkCreateView(APIView):
    def post(self, request):
        work = CreateWorkSerializer(data=request.data)
        if work.is_valid():
            work.save()
        return Response(status=201)
# {
# "name": "Mike",
# "lastname": "Make",
# "age": 21,
# "email": "Mike@mail.com",
# "telephone": +996 889 786787,
# "addres": "Osh",
# "conference": 1
# }