from django.shortcuts import render
from .models import Category, Movies

"""
kategori_list = ["dram", "macera", "romantik", "bilim kurgu"] 
film_list = [
    {
        "id": "1",
        "film_adi": "film1",
        "aciklama": "film1 aciklama",
        "resim": "1.jpg",
        "anasayfa": True
    },
    {
        "id": "2",
        "film_adi": "film2",
        "aciklama": "film2 aciklama",
        "resim": "2.jpg",
        "anasayfa": True   
    },
    {
        "id": "3",
        "film_adi": "film3",
        "aciklama": "film3 aciklama",
        "resim": "3.jpg",
        "anasayfa": False
    },
    {
        "id": "4",
        "film_adi": "film4",
        "aciklama": "film4 aciklama",
        "resim": "4.jpg",
        "anasayfa": False
    }
            ]

def home(request):
    
    data = {
        "kategoriler": kategori_list,
        "filmler": film_list
    }
    
    return render(request, "index.html", data)

def movies(request):
    
    data = {
        "kategoriler": kategori_list,
        "filmler": film_list
    }
    
    return render(request, "movies.html", data)
def moviedetails(request, id):
    
    data = {
        "id": id
    }
    
    return render(request, "details.html", data)
"""
    
def home(request):
    
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movies.objects.all()
    }
    
    return render(request, "index.html", data)
    
def movies(request):
    
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": Movies.objects.all()
    }
    
    return render(request, "movies.html", data)

def moviedetails(request, id):
    
    data = {
        "movie": Movies.objects.get(id=id)
    }
    
    return render(request, "details.html", data)