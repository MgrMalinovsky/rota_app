# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import render
import datetime
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'user_ex/index.html')

def calendar(request):
    return render(request, 'events/calendar.html', {})