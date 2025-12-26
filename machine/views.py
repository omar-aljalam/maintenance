from rest_framework import generics

from .models import Machine, MachineType
from .serializers import MachineSerializer, MachineTypeSerializer

class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineTypeListCreateView(generics.ListCreateAPIView):
    queryset = MachineType.objects.all()
    serializer_class = MachineTypeSerializer

class MachineTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MachineType.objects.all()
    serializer_class = MachineTypeSerializer