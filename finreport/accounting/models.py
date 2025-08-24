from django.db import models
from django.contrib.auth.models import User

# ====================================================
#  ACCOUNTING : Comptabilité
# ====================================================


class Exercise(models.Model):
    """Exercice comptable (N, N-1)."""
    company = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="exercises")
    year = models.IntegerField()
    is_closed = models.BooleanField(default=False)

    class Meta:
        unique_together = ("company", "year")

    def __str__(self):
        return f"{self.company.name} - Exercice {self.year}"


class Account(models.Model):
    """Plan comptable (SYSCOHADA ou autre)."""
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="accounts")
    number = models.CharField(max_length=20)  # Exemple: 211, 512, 401...
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")

    class Meta:
        unique_together = ("exercise", "number")

    def __str__(self):
        return f"{self.number} - {self.name}"


class TrialBalance(models.Model):
    """Balance importée à 6 colonnes (débits, crédits, soldes)."""
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="trial_balances")
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="trial_balances")
    opening_debit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    opening_credit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    movement_debit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    movement_credit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    closing_debit = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    closing_credit = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    def __str__(self):
        return f"Balance {self.exercise.year} - {self.account.number}"


class JournalEntry(models.Model):
    """Écritures comptables (simplifié)."""
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="journal_entries")
    date = models.DateField()
    description = models.TextField()
    debit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="debit_entries")
    credit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="credit_entries")
    amount = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.description} ({self.amount})"


class Closure(models.Model):
    """Clôture d'exercice comptable."""
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE, related_name="closure")
    closed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Clôture {self.exercise.year}"
