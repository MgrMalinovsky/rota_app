from datetime import date
from django.conf import settings
from django.shortcuts import render
from .forms import DateForm
from events.models import worktime



def post(request):
        text = 1
        form = DateForm(request.POST)
        model = worktime
        if form.is_valid():
            text = form.cleaned_data['date']
        if model.objects.filter(date=text).exists:
                o = model.objects.get(date=text)
                o.workers.add(request.user.id)
        else:
                query = worktime(date=text)
                query.save()
                query.workers.add(request.user.id)
        args = {'form': form, 'text': text}
        return render(request, 'workers/calendar.html', args)