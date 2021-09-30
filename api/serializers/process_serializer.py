from api.models.process_model import GetProcess, PostProcess
from rest_framework import serializers


class GetProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model=GetProcess
        fields = '__all__'
        depth=2



class PostProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostProcess
        fields = '__all__'
        