from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import DoctorSerializer, DepartmentSerializer, DepartmentIDSerializer
from rest_framework.response import Response
from .models import Doctor, Department
from rest_framework import generics

# Create your views here.
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

@method_decorator(cache_control(no_cache=True, no_store=True, must_revalidate=True), name='dispatch')
class MyView(TemplateView):
    template_name = 'index.html'


@api_view(['GET', 'POST'])
def enter_dep(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# (['POST'])
class CreateDoctor(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Record created successfully!'})
        else:
            return Response(serializer.errors, status=400)

class Enter_Doctor(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    # def perform_create(self, serializer):
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data) 
    #     else:
    #         return HttpResponse("not found", status=404)

@api_view(['GET'])
def get_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_dep(request):
    doctors = Department.objects.all()
    serializer = DepartmentSerializer(doctors, many=True)
    return Response(serializer.data)


class Dep_id(generics.RetrieveAPIView):
    serializer_class = DepartmentIDSerializer
    queryset = Department.objects.all()
    lookup_field = 'Name'