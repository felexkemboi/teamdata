from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static

urlpatterns = [
    path('email/',             views.email,    name='email'),
]
"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""