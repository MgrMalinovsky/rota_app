from django.urls import path
from . import views
app_name = 'managers'
urlpatterns = [

    path('', views.main, name="main"),
    path('checkworkers', views.checkworkers, name='checkworkers'),
    path('checkrota', views.checkrota, name='checkrota'),
]