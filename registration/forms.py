from django import forms
from django.forms import ModelForm
from .models import offreStage, user_profile

class user_profileForm(ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = user_profile
        fields = ['description','isCE','email','site']
        labels = {
            'isCE':'Êtes vous contact entreprise?',
            
        }
class offreStageForm(ModelForm):
    class Meta:
        model = offreStage
        fields = ['nom','description','datedebut','datefin','domaine','typeoffre']
    
        
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Selectionner un fichier .pdf',
        
    )