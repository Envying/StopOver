from django.shortcuts import render
from django.http import HttpResponse
from map.models import Car

def home(request):
	# Get all car objects from db
	cars = Car.objects.filter(available=True)

	if request.method == "POST":
		car_number_plate = request.POST.get('number_plate_id', None) # Set number_plate value
		set_car = Car.objects.get(number_plate=car_number_plate) # Set Car
		set_car.available = False # Change available to False
		set_car.save()
	else:
		# Argument to contain list of our car model
		args = {'cars': cars }
	return render(request, 'map/homepage.html', args)

def get_mylocation(request):
    if request.GET.get('find-me'):
        longitude = request.COOKIES.get('longitude', '')
        latitude = request.COOKIES.get('latitude', '')
    return render(request, 'map/homepage.html',
                {'longitude' :longitude,
                 'latitude' :latitude})
