from django.shortcuts import render, redirect
from django.http import HttpResponse
from map.models import Car
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView

from map.forms import CarForm

class HomePageView(TemplateView):
	template_name = 'map/homepage.html'

	def get_context_data(self, *args, **kwargs):
		print("get_context_data")
		numberplate = self.request.GET.get("number_plate")
		if numberplate != None:
			set_car = Car.objects.get(number_plate=numberplate)
			print(set_car.brand)

		context = super(HomePageView, self).get_context_data(*args, **kwargs)
		context['cars'] = Car.objects.filter(available=True)
		return context
