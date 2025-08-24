from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Company  # ajoute cette importation

# On utilisera plus tard le modèle Company pour lier les sociétés
# from companies.models import Company  

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('comptable', 'Comptable'),
        ('auditeur', 'Auditeur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    companies = models.ManyToManyField(Company, related_name='users')  # on l'ajoutera après création de l'app companies

    def __str__(self):
        return f"{self.username} ({self.role})"

