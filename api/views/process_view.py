from api.models.process_model import Process
from api.serializers.process_serializer import GetProcessSerializer, PostProcessSerializer
from rest_framework import generics



class ProcessList(generics.ListCreateAPIView):
    queryset = Process.objects.all()
    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return GetProcessSerializer
        else:
            return PostProcessSerializer




class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return GetProcessSerializer
        else:
            return PostProcessSerializer

