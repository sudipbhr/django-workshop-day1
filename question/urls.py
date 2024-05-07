
from django.urls import path, include
from django.http import HttpResponse
from question import views


urlpatterns = [
    path('question/', views.question),
    path('answer/', views.answer)
]
