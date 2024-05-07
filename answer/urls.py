
from django.urls import path, include
from django.http import HttpResponse
from answer import views



urlpatterns = [
   path('answer1/', views.answer),
]
