from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def question(request):
    return HttpResponse("What is your name? ")


def answer(request):
    return HttpResponse("My name is Sudip")