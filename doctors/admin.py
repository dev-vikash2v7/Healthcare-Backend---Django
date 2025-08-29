from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'license_number', 'phone_number', 'years_of_experience', 'is_available', 'created_by', 'created_at')
    list_filter = ('specialization', 'gender', 'is_available', 'created_at')
    search_fields = ('first_name', 'last_name', 'license_number', 'phone_number', 'email', 'specialization', 'created_by__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('created_by', 'first_name', 'last_name', 'specialization', 'license_number', 'gender', 'date_of_birth')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'email', 'address')
        }),
        ('Professional Information', {
            'fields': ('years_of_experience', 'education', 'certifications', 'languages_spoken', 'consultation_fee')
        }),
        ('Status', {
            'fields': ('is_available',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
