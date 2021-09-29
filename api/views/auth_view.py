from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ZetaBackend import settings
from api.backends import LDAPBackend


class AuthenticationView(APIView):

    def post(self, request):
        data = request.data
        try:
            LDAPBackend.authenticate(username=data['username'],
                                     password=data['password'])
            return Response({"ApiKey": settings.API_KEY, 'userDepartment': 'nothing yet'},
                            status=status.HTTP_201_CREATED)
        except ImportError:
            return Response({'error': ImportError.msg}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)