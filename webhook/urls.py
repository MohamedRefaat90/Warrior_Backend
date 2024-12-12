from django.urls import path
from .views import handle_webhook

urlpatterns = [
    path('', handle_webhook, name='webhook'),
]