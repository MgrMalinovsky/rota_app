
from django.urls import path
from . import views
app_name = 'workers'
urlpatterns = [

    path('', views.post, name="post"),
    path('check', views.check, name='check'),
]
