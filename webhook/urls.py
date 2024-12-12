from django.urls import path,include
from .views import handle_webhook
urlpatterns = [
    path('',handle_webhook,name='webhook'),
]
