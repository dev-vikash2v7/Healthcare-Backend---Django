from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    SPECIALIZATION_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Endocrinology', 'Endocrinology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Neurology', 'Neurology'),
        ('Oncology', 'Oncology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Psychiatry', 'Psychiatry'),
        ('Radiology', 'Radiology'),
        ('Surgery', 'Surgery'),
        ('Urology', 'Urology'),
        ('Other', 'Other'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    license_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    years_of_experience = models.PositiveIntegerField()
    education = models.TextField()
    certifications = models.TextField(blank=True, null=True)
    languages_spoken = models.TextField(blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialization}"

    @property
    def full_name(self):
        return f"Dr. {self.first_name} {self.last_name}"

    @property
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
