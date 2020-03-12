from django.shortcuts import render
from .forms import DateForm, grade_choiceForm, add_commentForm
from events.models import worktime, grading, commenting
from django_tables2 import SingleTableView
from .tables import PersonTable


def post(request):
    added_comment = ''
    text = '1990-01-01'
    selected_grade = 5
    form = DateForm(request.POST)
    model = worktime, grading
    if form.is_valid():
        text = form.cleaned_data['date']
    try:
        o = worktime.objects.get(date=text)
        o.workers.add(request.user.id)
        var = 1
    except worktime.DoesNotExist:
        query = worktime(date=text)
        query.save()
        query.workers.add(request.user.id)
        var = 0
    grade_form = grade_choiceForm(request.POST)
    if grade_form.is_valid():
        selected_grade = grade_form.cleaned_data['grades']
    choice = grading.objects.get(choice_text=selected_grade)
    choice.rate += 1
    choice.save()
    comment_form = add_commentForm(request.POST)
    if comment_form.is_valid():
        added_comment = comment_form.cleaned_data['comment']
    add_comment = commenting(comment=added_comment)
    add_comment.save()

    return render(request, 'workers/calendar.html', locals())


def check(request):
    model = worktime
    var = model.objects.filter(workers=request.user.id)
    return render(request, 'workers/check.html', locals())


class PersonListView(SingleTableView):
    model = worktime
    table_class = PersonTable
    template_name = 'workers/check.html'


