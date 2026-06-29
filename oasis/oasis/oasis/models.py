from django.db import models
from accounts.models import User

class Transaction(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En attente'),
        ('reussi', 'Réussi'),
        ('echoue', 'Échoué'),
    )
    METHODE_CHOICES = (
        ('orange_money', 'Orange Money'),
        ('mtn_momo', 'MTN MoMo'),
        ('moov_money', 'Moov Money'),
        ('wave', 'Wave'),
        ('carte_bancaire', 'Carte Bancaire'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    methode = models.CharField(max_length=30, choices=METHODE_CHOICES)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    reference = models.CharField(max_length=100, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.montant} FCFA - {self.methode}"


class PlanAbonnement(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    duree_jours = models.IntegerField()
    description = models.TextField(blank=True)
    est_actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nom} - {self.prix} FCFA"