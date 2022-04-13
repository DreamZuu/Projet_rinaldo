
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator



## offre de stage
class offreStage(models.Model):

    nom = models.CharField(max_length=100)
    description = models.TextField(null=True)
    datedebut = models.DateField(blank=True, null=True)
    datefin = models.DateField(blank=True, null=True)
    typeoffre = models.CharField(max_length=150, null=True)
    domaine = models.CharField(max_length=100, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name="offrestage", null=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

## Profile d'un utilisateur
class user_profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(null=True)
    isCE = models.BooleanField(default=False)
    site = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Document(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doc")
    docfile = models.FileField(upload_to='documents/%Y/%m/%d', validators=[FileExtensionValidator( ['pdf'] )])