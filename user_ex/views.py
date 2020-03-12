from django.shortcuts import render
from django import template


def index(request):
    return render(request, 'user_ex/index.html')



