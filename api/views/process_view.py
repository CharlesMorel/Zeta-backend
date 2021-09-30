from os import system
from api.models.process_model import GetProcess, PostProcess
from api.serializers.process_serializer import GetProcessSerializer, PostProcessSerializer
from rest_framework import generics
from api.z_encrypt import z_encrypt, z_decrypt
from django.http import HttpResponse, response
import json, logging
class ProcessList(generics.ListCreateAPIView):
    """
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if (self.request.method == 'POST'):
            request.data=json.dumps("".join(z_decrypt(request.data["data"])))
            response = self.get_response(request)
            print(response)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    """


    def get_queryset(self):
        if (self.request.method == 'GET'):
            return GetProcess.objects.all()
        else:
            return PostProcess.objects.all()

    def get_serializer_class(self):
    
        if (self.request.method == 'GET'):
                
            return GetProcessSerializer
        else:

            return PostProcessSerializer


    


class ProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        if (self.request.method == 'GET'):
            return PostProcess.objects.all()
        else:
            return PostProcess.objects.all()

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return PostProcessSerializer
        else:
            return PostProcessSerializer
    """
    def finalize_response(self, request, response, *args, **kwargs):
        encrypt_data=z_encrypt(json.dumps(response.data))
        return HttpResponse(encrypt_data)
    """

    """
    CHIFFREMENT
    
    def initialize_request(self, request, *args, **kwargs):        
        request.data=z_decrypt(json.dumps(request.data))
        return request

   def finalize_response(self, request, response, *args, **kwargs):
        encrypt_data=z_encrypt(json.dumps(response.data))
        return HttpResponse(encrypt_data)

    """
