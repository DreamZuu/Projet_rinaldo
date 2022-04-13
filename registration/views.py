from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from registration.forms import DocumentForm, offreStageForm, user_profileForm
from registration.models import  Document, offreStage, user_profile



## Login view
def login(request):
    return render(request, "registration/login.html", {})

## Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            ut = user_profile(user = user)
            user.save()
            ut.save()

            auth_login(request, user)
            return redirect('edit')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def edit(request):
    UP= user_profile.objects.get(user = request.user)
    form = user_profileForm(instance=UP)
    if request.method == 'POST':
        form = user_profileForm(request.POST, instance=UP)
        if form.is_valid():
            e = form.cleaned_data["email"]
            request.user.email = e
            
            form.save()
            request.user.save()

            return redirect('profile')

    return render(request, 'registration/edit.html', {'form': form})

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = Document.objects.get(user = request.user)
            if doc == None:
                newdoc = Document(user =request.user,docfile = request.FILES['docfile'])
                print(newdoc)
                newdoc.save()
            else:
                doc.delete()
                newdoc = Document(user =request.user,docfile = request.FILES['docfile'])
                print(newdoc)
                newdoc.save()

            # Redirect to the document list after POST
        return redirect('upload') 
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.get(user = request.user)
    return render(request, 'registration/upload.html', {'documents':documents,'form':form})



def addoffre(request):
    current_usr = request.user
    if request.method == 'POST':
        form = offreStageForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["nom"]
            d = form.cleaned_data["description"]
            dd = form.cleaned_data["datedebut"]
            df = form.cleaned_data["datefin"]
            do = form.cleaned_data["domaine"]
            to = form.cleaned_data["typeoffre"]
            OS = offreStage(nom=n,description =d,datedebut =dd,datefin=df,domaine =do,typeoffre=to, auteur=current_usr)
            OS.save()
           
        return redirect('mesoffres')    
    else:
       form = offreStageForm() 
    
    ## Affichage des offres de l'utilisateur
    all_offre= offreStage.objects.filter(auteur = current_usr)
    mynboffre = offreStage.objects.filter(auteur = current_usr, is_archived = False).count()
    return render(request, 'registration/mesOffres.html', {'alloffre':all_offre, 'mynboffre':mynboffre, 'form':form})


def modifierOffre(request, pk):
    myoffre = offreStage.objects.get(id=pk)
    form = offreStageForm(instance=myoffre)
    if request.method == 'POST':
        form = offreStageForm(request.POST, instance=myoffre)
        if form.is_valid():
           form.save()
        return redirect('mesoffres')
        
    return render(request, 'registration/modifierOffre.html', {'form':form})


def deleteOffre(request, pk):
    myoffre = offreStage.objects.get(id=pk)
    if request.method == 'POST':
        myoffre.is_archived = True
        myoffre.save()
        return redirect('mesoffres')


    return render(request, 'registration/deleteOffre.html', {'myoffre':myoffre})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name="registration/profile.html"



