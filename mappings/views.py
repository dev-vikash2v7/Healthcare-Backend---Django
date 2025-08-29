from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingListSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientDoctorMappingSerializer

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PatientDoctorMappingListSerializer
        return PatientDoctorMappingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({
                    'message': 'Doctor assigned to patient successfully',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({
                    'message': 'This doctor is already assigned to this patient',
                    'errors': {'non_field_errors': ['Duplicate assignment']}
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'Error assigning doctor to patient',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class MappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientDoctorMappingSerializer

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    def get_object(self):
        mapping_id = self.kwargs.get('pk')
        return get_object_or_404(PatientDoctorMapping, id=mapping_id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Mapping updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Error updating mapping',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({
            'message': 'Doctor removed from patient successfully'
        }, status=status.HTTP_204_NO_CONTENT)


class PatientDoctorsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientDoctorMappingListSerializer

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)
