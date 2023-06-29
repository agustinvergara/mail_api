from rest_framework.views import APIView
from rest_framework.response import Response
from mailsender.serializers import ClienteSerializer
from django.core.mail import send_mail
from django.conf import settings

class ClienteContactoView(APIView):
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Envío del correo electrónico
            subject = 'Nuevo Lead del landing page'
            message = f'Nombre: {serializer.data["nombre"]}\nApellido: {serializer.data["apellido"]} \nCorreo: {serializer.data["mail"]}\nNumero: {serializer.data["cell"]}\n Mensaje: {serializer.data["mensaje"]}'
            send_mail(subject, message, 'agustin.vergara.ruiz@gmail.com', ['agus20060@hotmail.com'], fail_silently=False,)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)