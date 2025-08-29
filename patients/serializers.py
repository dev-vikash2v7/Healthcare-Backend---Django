from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    age = serializers.ReadOnlyField()
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = [
            'id', 'created_by', 'first_name', 'last_name', 'full_name', 'date_of_birth', 
            'age', 'gender', 'blood_group', 'phone_number', 'email', 'address',
            'emergency_contact_name', 'emergency_contact_phone', 'medical_history',
            'allergies', 'current_medications', 'insurance_provider', 'insurance_number',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class PatientListSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    age = serializers.ReadOnlyField()
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = [
            'id', 'created_by', 'first_name', 'last_name', 'full_name', 'date_of_birth',
            'age', 'gender', 'blood_group', 'phone_number', 'email', 'created_at'
        ]
