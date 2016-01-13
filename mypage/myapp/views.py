from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render



def main_page(request):
    return render(request, 'myapp/index.html')


def maps_page(request):
	return render(request, 'myapp/maps.html')