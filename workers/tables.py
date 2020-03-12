import django_tables2 as tables
from events.models import worktime


class PersonTable(tables.Table):
    class Meta:
        model = worktime
        fields = ('all_staff', )
        template_name = "django_tables2/bootstrap.html"
