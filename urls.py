from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.liste_plans, name='liste_plans'),
    path('souscrire/', views.souscrire, name='souscrire'),
    path('transactions/', views.liste_transactions, name='liste_transactions'),
    path('transactions/<int:pk>/', views.detail_transaction, name='detail_transaction'),
]