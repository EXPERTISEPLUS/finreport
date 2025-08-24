from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True, null=True)
    nif = models.CharField(max_length=50, blank=True, null=True)  # Numéro d'identification fiscale
    currency = models.CharField(max_length=10, default='GNF')  # Devise
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

