from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.UserModel import LdapGroup
from django.core import serializers
from api.serializers.LdapGroupSerializer import LdapGroupSerializer


class AuthenticationView(APIView):

    def post(self, request):
        data = request.data
        try:
            result = serializers.serialize(LdapGroupSerializer, LdapGroup.objects.all())
            return Response(result, status=status.HTTP_201_CREATED)
        except ImportError:
            print(ImportError.msg)


class AuthenticationDetailView(APIView):
    def post(self, request):
        return Response("yes", status=status.HTTP_201_CREATED)