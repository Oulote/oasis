from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/paiements/', include('paiements.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('reglement/', TemplateView.as_view(template_name='reglement.html'), name='reglement'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
