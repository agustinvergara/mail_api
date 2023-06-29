from django.urls import path
from mailsender.views import ClienteContactoView

urlpatterns = [
    path('api/contacto/', ClienteContactoView.as_view(), name='cliente_contacto'),
]