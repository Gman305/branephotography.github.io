from django.shortcuts import render, redirect

from BranePhr.forms import CarouselForm, PhotoForm
from BranePhr.models import *

# Create your views here.

def index(request):
    carousel=Carousel.objects.all().order_by('-id')
    return render(request,'index.html',{'carousels':carousel})

def carousel_gallery(request,carousel_id):
    carousel=Carousel.objects.get(id=carousel_id)
    image=Images.objects.filter(carousel=carousel)
    return render(request,'carousels.html',{'images':image})

def add_carousel(request):
    if request.method == "POST":
        form = CarouselForm(request.POST, request.FILES)
        if form.is_valid():
            carousel = form.save(commit=False)
            carousel.save()
        return redirect('home')
    return render(request,'add_carousels.html',{'form':CarouselForm()})

def add_image(request):
    if request.method == "POST":
        images=request.FILES.getlist('image')
        form = PhotoForm(request.POST, request.FILES)
        for img in images:
            image=Images()
            image.carousel=Carousel.objects.get(id=request.POST['carousel'])
            image.image=img
            image.save()
        return redirect('home')
    return render(request,'add_images.html',{'form':PhotoForm()})

def contact(request):
    return render(request,'contactDetails.html')

def gallery(request):
        carousel = Carousel.objects.all().order_by('-id')
        return render(request, 'gallery.html', {'carousels': carousel})