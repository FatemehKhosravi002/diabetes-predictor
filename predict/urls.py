from django.contrib import admin
from django.urls import path , include
from .views import PredictView

urlpatterns = [
    path('predict' , PredictView),
]
