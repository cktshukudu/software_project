from django.urls import path
from .views import Dep_id, Enter_Doctor, MyView, CreateDoctor
from . import views

urlpatterns = [
     path('', MyView.as_view()),
     path('enterdoctor/', CreateDoctor.as_view(), name='enterdoctor'),
     path('enterdep/', views.enter_dep, name='enterdep'),
     path('dep/', views.get_dep, name='enterdep'),
     path('doctors/', views.get_doctors, name='doctors'),
     path('getdepid/<str:Name>', Dep_id.as_view(), name='dep_id'),
]