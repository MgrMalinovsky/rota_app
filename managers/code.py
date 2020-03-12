from events.models import worktime, workersinrota
import random

def calculating():
    day = worktime.objects.filter(date=text)
    number_wor = worktime.workers.get(date=day)
    num_wor = len(number_wor)
    number_man = day.workersInDay
    try:
        query = workersinrota.objects.get(date=text)
    except workersinrota.DoesNotExist:
        query = workersinrota(date=text)
        query.save()
    number_man = day.workersInDay
    if num_wor < number_man:
        workersinrota.workers.m2mfield.add(number_wor)
    elif number_wor == number_man:
        workersinrota.workers.m2mfield.add(number_wor)
    else:
            num_temp = 0
            while num_temp < number_wor:
                temp_work = random.choice(number_wor)
                if workersinrota.workers.filter(username=temp_work).exists():
                    pass
                else:
                    workersinrota.workers.add(temp_work)
                    num_temp = num_temp + 1






