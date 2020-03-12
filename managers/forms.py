from django import forms
from django.contrib.auth.models import User
from events.models import worktime
import django_filters


class SelectworkersForm(forms.Form):
    worklist = forms.ModelChoiceField(queryset=worktime.objects.all(), to_field_name="date")
    amount = forms.IntegerField()



#worklist = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='workers'))