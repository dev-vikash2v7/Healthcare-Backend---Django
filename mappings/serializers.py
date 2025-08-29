from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientListSerializer
from doctors.serializers import DoctorListSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    assigned_by = serializers.ReadOnlyField(source='assigned_by.username')
    patient_details = PatientListSerializer(source='patient', read_only=True)
    doctor_details = DoctorListSerializer(source='doctor', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'assigned_by', 'assigned_date', 'status',
            'notes', 'created_at', 'updated_at', 'patient_details', 'doctor_details'
        ]
        read_only_fields = ['id', 'assigned_by', 'assigned_date', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['assigned_by'] = self.context['request'].user
        return super().create(validated_data)


class PatientDoctorMappingListSerializer(serializers.ModelSerializer):
    assigned_by = serializers.ReadOnlyField(source='assigned_by.username')
    patient_name = serializers.CharField(source='patient.full_name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.full_name', read_only=True)
    doctor_specialization = serializers.CharField(source='doctor.specialization', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'patient_name', 'doctor_name', 'doctor_specialization',
            'assigned_by', 'assigned_date', 'status', 'created_at'
        ]
