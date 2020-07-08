from django.shortcuts import render, redirect

from myapp.models import *


def show_about_page(request):
    print("About Page request")
    name = "Abhishek"
    link = 'https://github.com/Abhishek-121'

    data = {
        'name' : name,
        'link' : link
    }

    return render(request,"about.html",data)


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    # Fetch all the Images from the DB (sqlite3)
    data = {'images':images, 'cats':cats}
    return render(request,"home.html", data)

def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()

    category = Category.objects.get(pk = cid)

    # filter(field = value)

    images = Image.objects.filter(cat = category)

    # Fetch all the Images from the DB (sqlite3)

    data = {'images':images, 'cats':cats}

    return render(request,"home.html", data)

def home(request):
    return redirect('/home')



