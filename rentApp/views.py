from django.shortcuts import render, get_object_or_404, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Rower, Salon
from .forms import RowerForm, SalonForm, WypozyczeniaForm
from django.db.models import Q


def all_bikes(request):
    bikes_list = Rower.objects.all()
    now = datetime.now()
    current_year = now.year
    return render(request, 'rent/bikes.html', {
        'bikes_list': bikes_list,
        'current_year': current_year,
    })


def list_salons(request):
    salon_list = Salon.objects.all()
    return render(request, 'rent/list_salon.html', {
        'salon_list': salon_list,
    })


def show_salon(request, id_salonu):
    salon = get_object_or_404(Salon, id_salonu=id_salonu)
    return render(request, 'rent/show_salon.html', {'salon': salon})


def add_order(request):
    submitted = False
    if request.method == 'POST':
        form = WypozyczeniaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_order?submitted=True')
    else:
        form = WypozyczeniaForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'rent/add_order.html',
                  {'form': form,
                   'submitted': submitted})


def add_bike(request):
    submitted = False
    if request.method == 'POST':
        form = RowerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_bike?submitted=True')
    else:
        form = RowerForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'rent/add_bike.html',
                  {'form': form,
                   'submitted': submitted})


# def show_salon(request, id_salonu):
#     salon = Salon.objects.get(pk=id_salonu)
#     return render(request, 'rent/show_salon.html', {
#         'salon': salon,
#     })


def update_salon(request, id_salonu):
    salon = get_object_or_404(Salon, id_salonu=id_salonu)
    form = SalonForm(request.POST or None, instance=salon)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/list_salon/')
    return render(request, 'rent/update_salon.html', {'salon': salon, 'form': form})


def delete_salon(request, id_salonu):
    salon = get_object_or_404(Salon, id_salonu=id_salonu)
    salon.delete()
    return redirect('/list_salon/')


def add_salon(request):
    submitted = False
    if request.method == 'POST':
        form = SalonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_salon?submitted=True')
    else:
        form = SalonForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'rent/add_salon.html',
                  {'form': form,
                   'submitted': submitted})


def search_bike(request):
    if request.method == "POST":
        searched = request.POST['searched']
        bikes = Rower.objects.filter(
            Q(marka__contains=searched) | Q(kolor__contains=searched) | Q(rodzaj_roweru__contains=searched) | Q(
                material_ramy__contains=searched) | Q(koszt__contains=searched))
        return render(request, 'rent/search_bike.html', {'searched': searched, 'bikes': bikes})
    else:
        return render(request, 'rent/search_bike.html', {})


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
