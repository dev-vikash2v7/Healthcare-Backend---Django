from django.contrib import admin
from .models import PatientDoctorMapping


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_by', 'status', 'assigned_date')
    list_filter = ('status', 'assigned_date', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name', 'assigned_by__username')
    readonly_fields = ('assigned_date', 'created_at', 'updated_at')
    fieldsets = (
        ('Assignment Information', {
            'fields': ('patient', 'doctor', 'assigned_by', 'status')
        }),
        ('Additional Information', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('assigned_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
