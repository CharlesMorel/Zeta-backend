from api.models.frisbee_model import Frisbee
from api.models.frisbee_ingredient_model import PostFrisbeeIngredient, GetFrisbeeIngredient
from api.serializers.frisbee_serializer import GetFrisbeeSerializer, PostFrisbeeSerializer
from rest_framework import generics
from api.serializers.frisbee_ingredient_serializer import PostFrisbeeIngredientSerializer



class FrisbeeList(generics.ListCreateAPIView):
    queryset = Frisbee.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetFrisbeeSerializer
        if self.request.method == 'POST':
            return PostFrisbeeSerializer
        return PostFrisbeeSerializer



class FrisbeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Frisbee.objects.all()
    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return GetFrisbeeSerializer
        else:
            return PostFrisbeeSerializer


class FrisbeeIngredientList(generics.ListCreateAPIView):
    def get_queryset(self):
        if (self.request.method == 'GET'):
            queryset = GetFrisbeeIngredient.objects.all()
        else:
            queryset = PostFrisbeeIngredient.objects.all()
        return queryset

    serializer_class = PostFrisbeeIngredientSerializer


class FrisbeeIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        fri=self.request.query_params.get('fri')
        queryset=GetFrisbeeIngredient.objects.all().filter(Pfk_frisbee_id=fri, Pfk_ingredient_id=self.kwargs['pk'])
        return queryset
    serializer_class = PostFrisbeeIngredientSerializer

