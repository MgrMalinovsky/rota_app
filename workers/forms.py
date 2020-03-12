from django import forms
from events.models import grading

class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%d/%m/%Y'])

class grade_choiceForm(forms.Form):
    grades = forms.ModelChoiceField(queryset=grading.objects.all(), to_field_name='choice_text')


class add_commentForm(forms.Form):
    comment = forms.CharField(max_length=1000)