from rest_framework import serializers
from .models import Department, Doctor, Report, Reviews, Rooms, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
class DepartmentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id']
