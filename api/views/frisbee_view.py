from api.models.frisbee_model import Frisbee
from api.serializers.frisbee_serializer import FrisbeeSerializer
from rest_framework import generics


class FrisbeeList(generics.ListCreateAPIView):
    queryset = Frisbee.objects.all()
    serializer_class = FrisbeeSerializer


