from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ZetaBackend import settings
import ldap


class AuthenticationView(APIView):

    def post(self, request):
        data = request.data
        try:
            return Response(data["email"], status=status.HTTP_201_CREATED)
        except ImportError:
            pass


class AuthenticationDetailView(APIView):
    def post(self, request):
        return Response("yes", status=status.HTTP_201_CREATED)