from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from ZetaBackend import settings
from api.backends import LDAPBackend


class AuthenticationView(APIView):

    def post(self, request):
        data = request.data
        try:
            user_obj = LDAPBackend.authenticate(username=data['username'],
                                                password=data['password'])
            print('Logging user...')
            login(request, user_obj, backend="django.contrib.auth.backends.ModelBackend")
            print('User logged successfully')
            return Response({"ApiKey": settings.API_KEY, 'userDepartment': 'nothing yet'},
                            status=status.HTTP_201_CREATED)
        except ImportError:
            return Response({'error': ImportError.msg}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        logout(request)
        return Response({'detail': 'User logged out successfully.'}, status=status.HTTP_200_OK)

