from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    age = serializers.ReadOnlyField()
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Doctor
        fields = [
            'id', 'created_by', 'first_name', 'last_name', 'full_name', 'specialization',
            'license_number', 'phone_number', 'email', 'address', 'gender', 'date_of_birth',
            'age', 'years_of_experience', 'education', 'certifications', 'languages_spoken',
            'consultation_fee', 'is_available', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class DoctorListSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    age = serializers.ReadOnlyField()
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Doctor
        fields = [
            'id', 'created_by', 'first_name', 'last_name', 'full_name', 'specialization',
            'license_number', 'phone_number', 'email', 'gender', 'age', 'years_of_experience',
            'consultation_fee', 'is_available', 'created_at'
        ]
