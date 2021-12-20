from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Airplane, Country, Person, Ticket
from .forms import AirplaneForm, CountryForm, PersonForm, TicketForm


def index(request):
    ticket = Ticket.objects.all()
    return render(request, 'index.html', {'ticket': ticket})


def createTicket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = TicketForm()
    return render(request, "createTicket.html", {'form': form})


def displayAirplane(request):
    airplane = Airplane.objects.all()
    return render(request, "displayAirplane.html", {'airplane': airplane})


def createAirplane(request):
    if request.method == "POST":
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = AirplaneForm()
    return render(request, "createAirplane.html", {'form': form})


def displayCountry(request):
    сountry = Country.objects.all()
    return render(request, "displayCountry.html", {'сountry': сountry})


def createCountry(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = CountryForm()
    return render(request, "createCountry.html", {'form': form})


def displayPerson(request):
    person = Person.objects.all()
    return render(request, "displayPerson.html", {'person': person})


def createPerson(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PersonForm()
    return render(request, "createPerson.html", {'form': form})
