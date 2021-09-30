from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from ZetaBackend import settings
from api.backends import LDAPBackend
from api.models import LoginTrial
import datetime


class AuthenticationView(APIView):

    def post(self, request):
        data = request.data
        try:
            date = datetime.datetime.utcnow()
            logs = LoginTrial.objects.filter(username=data['Username'],
                                             try_at__gte=date - datetime.timedelta(minutes=30))

            fail_since_success = 0
            reach_success = False
            if len(logs) > 0:
                for log in logs:
                    if reach_success is False & log.success is False:
                        fail_since_success += 1

            if fail_since_success >= 5:
                return Response({"Error": "You have reached 5 login trials for the last 30 minutes. "
                                          "You can try again later."}, status=status.HTTP_401_UNAUTHORIZED)

            user_obj = LDAPBackend.authenticate(username=data['Username'],
                                                password=data['Password'])
            # login(request, user_obj, backend="django.contrib.auth.backends.ModelBackend")
            return Response({"ApiKey": settings.API_KEY, 'userDepartment': 'nothing yet'},
                            status=status.HTTP_201_CREATED)
        except ValueError:
            return Response({"Error": "Incorrect username or password."}, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
        # try:
            # logout(request)
        # except ImportError:
        #     return Response({'error': 'Cannot log out user.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # return Response({'detail': 'User logged out successfully.'}, status=status.HTTP_200_OK)

