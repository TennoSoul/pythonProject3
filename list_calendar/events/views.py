from django.http import HttpResponseRedirect
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime, timedelta
from .models import Event
from .forms import EventForm


# Create your views here.
# Get current year and month
# views.py
now = datetime.now()
current_year = now.year
current_month = now.month

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/events_list.html', {
        'event_list': event_list

    })


def add_event(request):
    submitted = False
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    if month.isdigit():  # if month is a number
        month = calendar.month_name[int(month)]
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(year, month_number)
    return render(request, 'events/home.html', {
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,

    })
