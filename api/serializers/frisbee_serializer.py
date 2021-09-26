from api.models.frisbee_model import Frisbee
from rest_framework import serializers

class FrisbeeSerializer(serializers.ModelSerializer):
    frisbee=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Frisbee
        fields = ['id', 'name', 'description', 'pUHT', 'Range', 'frisbee_ref']