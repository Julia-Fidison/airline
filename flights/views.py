from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Airport, Flight, Passenger

# Create your views here.

def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        'flights': flights
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passenger = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        'flight':flight,
        'passengers': passengers,
        'non_passenger': non_passenger
    })


def book(request, flight_id):
    if request.method == "POST":

        flight = Flight.objects.get(pk=flight_id)

        passenger_id = int(request.POST["passenger"])

        passenger = Passenger.objects.get(pk=passenger_id)

        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))