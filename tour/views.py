from django.shortcuts import render
from .models import*
from .forms import BookingForm
# Create your views here.
def home(request):
	return render(request,"tour/home.html")

def about(request):
	return render(request,"tour/about.html")

def daytrip(request):
	return render(request,"tour/daytrip.html")

def index(request):
	return render(request,"tour/index.html")	

def gallery(request):
	return render(request,"tour/gallery.html")

def contact(request):
	return render(request,"tour/contact.html")

def destination(request):
	return render(request,"tour/destination.html")

def product_detail(request):
	return render(request,"tour/product_detail.html")

def product_detailone(request):
	return render(request,"tour/product_detailone.html")	

def product_detailtwo(request):
	return render(request,"tour/product_detailtwo.html")

def product_detailthree(request):
	return render(request,"tour/product_detailthree.html")

def product_detailfour(request):
	return render(request,"tour/product_detailfour.html")

def product_detailfive(request):
	return render(request,"tour/product_detailfive.html")					


def product_detailsix(request):
	return render(request,"tour/product_detailsix.html")

def product_detailseven(request):
	return render(request,"tour/product_detailseven.html")

def product_detaileight(request):
	return render(request,"tour/product_detaileight.html")

def product_detailnine(request):
	return render(request,"tour/product_detailnine.html")

def booking(request):

	form = BookingForm()

	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request,"tour/booking.html", context)				