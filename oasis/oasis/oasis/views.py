from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Transaction, PlanAbonnement
from accounts.models import Abonnement
from datetime import date, timedelta
import uuid

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste_plans(request):
    plans = PlanAbonnement.objects.filter(est_actif=True)
    data = [{
        'id': p.id,
        'nom': p.nom,
        'prix': str(p.prix),
        'duree_jours': p.duree_jours,
        'description': p.description,
    } for p in plans]
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def souscrire(request):
    user = request.user
    plan_id = request.data.get('plan_id')
    methode = request.data.get('methode')
    try:
        plan = PlanAbonnement.objects.get(pk=plan_id, est_actif=True)
        transaction = Transaction.objects.create(
            user=user,
            montant=plan.prix,
            methode=methode,
            statut='reussi',
            reference=str(uuid.uuid4())[:20],
        )
        Abonnement.objects.create(
            user=user,
            date_fin=date.today() + timedelta(days=plan.duree_jours),
            statut='actif',
            montant=plan.prix,
        )
        return Response({
            'message': 'Abonnement souscrit avec succès',
            'reference': transaction.reference,
            'date_fin': date.today() + timedelta(days=plan.duree_jours),
        }, status=201)
    except PlanAbonnement.DoesNotExist:
        return Response({'erreur': 'Plan introuvable'}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liste_transactions(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date_creation')
    data = [{
        'id': t.id,
        'montant': str(t.montant),
        'methode': t.methode,
        'statut': t.statut,
        'reference': t.reference,
        'date': t.date_creation,
    } for t in transactions]
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_transaction(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk, user=request.user)
        return Response({
            'id': transaction.id,
            'montant': str(transaction.montant),
            'methode': transaction.methode,
            'statut': transaction.statut,
            'reference': transaction.reference,
            'date': transaction.date_creation,
        })
    except Transaction.DoesNotExist:
        return Response({'erreur': 'Transaction introuvable'}, status=404)