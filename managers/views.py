from django.shortcuts import render
from .forms import SelectworkersForm
from workers.forms import grade_choiceForm, add_commentForm, DateForm
from events.models import worktime, grading, commenting, workersinrota

import random


def main(request):
    return render(request, 'managers/indexmenu.html')


def checkworkers(request):
    added_comment = ''
    selected_grade = 5
    selected_day = '1990-01-01'
    number = 1
    list1 = []
    form = SelectworkersForm(request.POST)
    model = worktime
    if form.is_valid():
        selected_day = form.cleaned_data['worklist'].date
        number = form.cleaned_data['amount']

        query = model.objects.get(date=selected_day)
        query.workersInDay = number
        query.save()
        list1 = query.workers.all()

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
    args = {'form': form, 'list1':list1}
    return render(request, 'managers/checkworkers.html', locals())


def checkrota(request):
    list1 = []
    text = '1990-01-01'
    form = DateForm(request.POST)
    model = worktime
    num_wor = 0
    number_wor = []
    if form.is_valid():
        text = form.cleaned_data['date']
    day = worktime.objects.get(date=text)
    number_wor = day.workers.all()
    num_wor = day.workers.count()
    number_man = day.workersInDay
    try:
        query = workersinrota.objects.get(date=text)
    except workersinrota.DoesNotExist:
        query = workersinrota(date=text)
        query.save()
    number_man = day.workersInDay
    if num_wor < number_man:
        for x in number_wor:
            query.workers.add(x)

    elif num_wor == number_man:
        for x in number_wor:
            query.workers.add(x)
    else:
        num_temp = query.workers.count()
        while num_temp < number_man:
            temp_work = random.choice(number_wor)
            if temp_work in query.workers.all() or temp_work == "manger1":
                pass
            else:
                query.workers.add(temp_work)
                num_temp = num_temp + 1
    if not text == '1990-01-01':
        list1 = query.workers.all()
    args = {'form': form, 'text': text, 'list1':list1}
    return render(request, 'managers/checkrota.html', locals())
