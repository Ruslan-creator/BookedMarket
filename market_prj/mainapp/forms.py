"""Формы используемые для страниц на сайте."""
from django import forms
from django.utils import timezone
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from mainapp.models import Accommodation
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from market_prj import settings

df = settings.DATE_INPUT_FORMATS


# class EventForm3(forms.ModelForm):
#     class Meta:
#         model = Accommodation
#         fields = ['name']
#         widgets = {
#             'name': DatePickerInput(),
#         }
class EventForm(forms.Form):
    date_from = forms.DateTimeField(
        label="Начало",
        input_formats=df,
        initial=lambda: timezone.now().astimezone().strftime(df[0]),
        widget=DateTimePickerInput(
            format=df[0],
            options={
                "locale": "ru",
                "showClose": True,
                "showClear": False,
                "showTodayButton": True,
            },
        ),
    )
    date_to = forms.DateTimeField(
        label="Конец",
        input_formats=df,
        initial=lambda: timezone.now().astimezone().strftime(df[0]),
        widget=DateTimePickerInput(
            format=df[0],
            options={
                "locale": "ru",
                "showClose": True,
                "showClear": False,
                "showTodayButton": True,
            },
        ),
    )
    format = forms.CharField(required=False)

