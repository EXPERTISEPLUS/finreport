from django.db import models
from django.contrib.auth.models import User

# ====================================================
#  CORE : Gestion multi-firmes (cabinet) et sociétés
# ====================================================

class Firm(models.Model):
    """Cabinet comptable qui gère plusieurs sociétés."""
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    """Une société cliente gérée par un cabinet."""
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name="companies")
    name = models.CharField(max_length=255)
    fiscal_year_start = models.DateField(help_text="Date de début de l’exercice fiscal")
    fiscal_year_end = models.DateField(help_text="Date de fin de l’exercice fiscal")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("firm", "name")

    def __str__(self):
        return f"{self.name} ({self.firm.name})"


class Membership(models.Model):
    """Lien utilisateur ↔ société avec rôle (ex: admin, comptable, auditeur)."""
    ROLE_CHOICES = [
        ("admin", "Administrateur"),
        ("accountant", "Comptable"),
        ("auditor", "Auditeur"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="accountant")

    class Meta:
        unique_together = ("user", "company")

    def __str__(self):
        return f"{self.user.username} - {self.company.name} ({self.role})"