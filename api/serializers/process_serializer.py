from api.models.process_model import Process
from rest_framework import serializers


class GetProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Process
        fields = '__all__'
        depth=2



class PostProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Process
        fields = '__all__'