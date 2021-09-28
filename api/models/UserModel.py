from ldapdb import models
from ldapdb.models.fields import CharField, IntegerField, ListField


class LdapGroup(models.Model):
    base_dn = "ou=Informatique,dc=killer-bee,dc=com"
    object_classes = ['user']

    gid = IntegerField(db_column='gidNumber', unique=True)
    name = CharField(db_column='cn', max_length=200, primary_key=True)
    members = ListField(db_column='memberUid')

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self.name)
