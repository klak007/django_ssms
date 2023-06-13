from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Rower


def all_bikes(request):
    bikes_list = Rower.objects.all()
    now = datetime.now()
    current_year = now.year
    return render(request, 'rent/bikes.html', {
        'bikes_list': bikes_list,
        'current_year': current_year,
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    title = 'Home Page'
    # convert month from name to number
    month_number = list(calendar.month_name).index(month.capitalize())
    month_number = int(month_number)
    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    # get the current year
    now = datetime.now()
    current_year = now.year

    # get current time
    time = now.strftime("%H:%M")
    return render(request, 'rent/home.html', {
        'title': title,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'time': time,
    })
# Create your views here.
