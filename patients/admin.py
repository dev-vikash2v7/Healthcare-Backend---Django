from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'gender', 'blood_group', 'phone_number', 'created_by', 'created_at')
    list_filter = ('gender', 'blood_group', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email', 'created_by__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('created_by', 'first_name', 'last_name', 'date_of_birth', 'gender', 'blood_group')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email', 'address')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone')
        }),
        ('Medical Information', {
            'fields': ('medical_history', 'allergies', 'current_medications')
        }),
        ('Insurance', {
            'fields': ('insurance_provider', 'insurance_number')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
