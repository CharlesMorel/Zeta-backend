from api.models.process_model import Process
from api.serializers.process_serializer import GetProcessSerializer, PostProcessSerializer
from rest_framework import generics
from api.z_encrypt import z_encrypt
from django.http import HttpResponse
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
    
    """
    CHIFFREMENT
    
    def initialize_request(self, request, *args, **kwargs):        
        request.data=z_decrypt(json.dumps(request.data))
        return request

    def finalize_response(self, request, response, *args, **kwargs):
        encrypt_data=z_encrypt(response.data)
        return HttpResponse(encrypt_data)

    """
