import datetime
import logging
import pytz
import ldap3
from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPBindError
from api.models import LoginTrial

from ZetaBackend import settings
from django.contrib.auth import get_user_model, get_user


logger = logging.getLogger(__name__)
UserModel = get_user_model()


class LDAPBackend:

    @staticmethod
    def authenticate(username=None, password=None, **kwargs):
        # set username to lowercase for consistency
        username = username.lower()
        # set your server
        print('Connecting to server...')
        server = Server(settings.AUTH_LDAP_SERVER_URI, port=settings.AD_LDAP_PORT, get_info=ldap3.ALL)
        print('Connected successfully.')
        logTrial = LoginTrial.objects.create(username=username, try_at=datetime.datetime.utcnow())
        try:
            print('Trying to create connection for user...')
            Connection(server, f"{username}@{settings.LDAP_DOMAIN}", password=password, auto_bind=True)
            print('Connection established successfully.')
            LoginTrial.objects.filter(id=logTrial.id).update(success=True)
            return True
        except ImportError:
            return False

        # user = UserModel.objects.update_or_create(username=username)

    @staticmethod
    def get_user(user_id):
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None