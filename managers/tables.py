import django_tables2 as tables
from events.models import worktime


class PersonTable(tables.Table):
    class Meta:
        model = worktime
        template_name = "django_tables2/bootstrap.html"
        field = ('workers')

