from rest_framework import serializers


class LdapGroupSerializer(serializers.Serializer):
    gid = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    members = serializers.ListField()
