from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMapping(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments_made')
    assigned_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['patient', 'doctor']
        ordering = ['-assigned_date']

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name} ({self.status})"

    @property
    def is_active(self):
        return self.status == 'active'
