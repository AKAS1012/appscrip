from django.shortcuts import render


# Create your views here.
def name(request):
	return render(request, "name.html")


def cricketer(request):
	return render(request, "cricketer.html")


def color(request):
	return render(request, "color.html")
