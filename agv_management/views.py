from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import agv_data, agv_identify
from .serializers import AgvIdentifySerializer, AgvDataserializer

# For Agv_identify restful API
class AgvIdentifyViewSet(viewsets.ModelViewSet):
    serializer_class = AgvIdentifySerializer
    queryset = agv_identify.objects.all()
    permission_classes = [IsAuthenticated]

# For Agv_data websocket 
class AgvDataViewSet(viewsets.ModelViewSet):
    
    serializer_class = AgvDataserializer
    queryset = agv_data.objects.all()
    
def index(request):
    return render(request, "agv_management/index.html")

def agv_data_realtime(request):
    return render(request, 'agv_data_realtime.html')
