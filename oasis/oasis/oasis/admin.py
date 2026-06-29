from django.contrib import admin
from .models import Transaction, PlanAbonnement

@admin.register(PlanAbonnement)
class PlanAbonnementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'duree_jours', 'est_actif')
    list_filter = ('est_actif',)
    search_fields = ('nom',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'montant', 'methode', 'statut', 'reference', 'date_creation')
    list_filter = ('statut', 'methode')
    search_fields = ('reference', 'user__username')