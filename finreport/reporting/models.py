from django.db import models
from django.contrib.auth.models import User

# ====================================================
#  REPORTING : États financiers
# ====================================================

class ReportTemplate(models.Model):
    """Modèle de plaquette (Bilan, CPC, TAFIRE, etc.)."""
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=[
        ("bilan", "Bilan"),
        ("cpc", "Compte de produits et charges"),
        ("taf", "Tableau Financier des Ressources et Emplois"),
    ])

    def __str__(self):
        return f"{self.name} ({self.type})"


class ReportLine(models.Model):
    """Ligne d'un état financier (ex: Actif immobilisé, Passif circulant)."""
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE, related_name="lines")
    code = models.CharField(max_length=20)  # ex: "ACTIF01"
    label = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"{self.label} ({self.code})"


class MappingAccountReport(models.Model):
    """Lien entre comptes comptables et lignes d'états financiers."""
    account = models.ForeignKey("Account", on_delete=models.CASCADE, related_name="mappings")
    line = models.ForeignKey(ReportLine, on_delete=models.CASCADE, related_name="mappings")

    def __str__(self):
        return f"{self.account.number} → {self.line.label}"


class FinancialStatement(models.Model):
    """Résultat généré (N et N-1)."""
    exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE, related_name="statements")
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE, related_name="statements")
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.template.name} - {self.exercise.year}"