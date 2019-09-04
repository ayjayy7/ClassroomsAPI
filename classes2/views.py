from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
 # RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
# from datetime import datetime
from classes.models import Classroom


from .serializers import ClassroomSerializer, ClassroomDetailsSerializer, ClassroomUpdateSerializer



class ClassroomList(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomDetails(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class ClassroomUpdate(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'



class ClassroomCreate(CreateAPIView):
    serializer_class = ClassroomUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ClassroomDelete(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


