
from django.shortcuts import render
from django.db.models import Q
from registration.models import offreStage

# Create your views here.
def index(request):
    return render(request, "main/index.html", locals())


def contact(request):
    return render(request, "main/contact.html", {})

def about(request):
    return render(request, "main/about.html", {})

def offre(request):
    search_offre = request.GET.get('search')

    if search_offre:
        all_offre = offreStage.objects.filter(Q(typeoffre__icontains=search_offre) | Q(nom__icontains=search_offre))
    else:
        all_offre= offreStage.objects.all()

    return render(request, "main/offre.html", {'offre':all_offre})


def detailOffre(request, pk):
    myoffre = offreStage.objects.get(id=pk)
    return render(request, "main/detailOffre.html", {'offres':myoffre})
