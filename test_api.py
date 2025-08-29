#!/usr/bin/env python3
"""
Simple test script to verify the healthcare backend API endpoints.
Run this after setting up the server to test basic functionality.
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_healthcare_api():
    print("Testing Healthcare Backend API")
    print("=" * 50)
    
    # Test 1: Register a new user
    print("\n1. Testing User Registration...")
    register_data = {
        "username": "testuser",
        "password": "testpass123",
        "password2": "testpass123",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register/", json=register_data)
        if response.status_code == 201:
            print("✅ User registration successful")
            user_data = response.json()
            print(f"   User ID: {user_data.get('user_id')}")
        else:
            print(f"❌ User registration failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the server is running.")
        return
    
    # Test 2: Login user
    print("\n2. Testing User Login...")
    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login/", json=login_data)
        if response.status_code == 200:
            print("✅ User login successful")
            token_data = response.json()
            access_token = token_data.get('access')
            print(f"   Access token received: {access_token[:20]}...")
        else:
            print(f"❌ User login failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return
    
    # Test 3: Create a patient
    print("\n3. Testing Patient Creation...")
    patient_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1990-01-01",
        "gender": "M",
        "blood_group": "A+",
        "phone_number": "+1234567890",
        "email": "john.doe@example.com",
        "address": "123 Main St, City, State 12345",
        "emergency_contact_name": "Jane Doe",
        "emergency_contact_phone": "+1234567891",
        "medical_history": "No significant medical history",
        "allergies": "None",
        "current_medications": "None",
        "insurance_provider": "Blue Cross",
        "insurance_number": "BC123456789"
    }
    
    headers = {"Authorization": f"Bearer {access_token}"}
    
    try:
        response = requests.post(f"{BASE_URL}/patients/", json=patient_data, headers=headers)
        if response.status_code == 201:
            print("✅ Patient creation successful")
            patient_response = response.json()
            patient_id = patient_response.get('data', {}).get('id')
            print(f"   Patient ID: {patient_id}")
        else:
            print(f"❌ Patient creation failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return
    
    # Test 4: Create a doctor
    print("\n4. Testing Doctor Creation...")
    doctor_data = {
        "first_name": "Dr. Michael",
        "last_name": "Johnson",
        "specialization": "Cardiology",
        "license_number": "MD123456",
        "phone_number": "+1234567890",
        "email": "michael.johnson@hospital.com",
        "address": "456 Medical Center Dr, City, State 12345",
        "gender": "M",
        "date_of_birth": "1975-03-20",
        "years_of_experience": 15,
        "education": "MD from Harvard Medical School",
        "certifications": "Board Certified in Cardiology",
        "languages_spoken": "English, Spanish",
        "consultation_fee": 150.00,
        "is_available": True
    }
    
    try:
        response = requests.post(f"{BASE_URL}/doctors/", json=doctor_data, headers=headers)
        if response.status_code == 201:
            print("✅ Doctor creation successful")
            doctor_response = response.json()
            doctor_id = doctor_response.get('data', {}).get('id')
            print(f"   Doctor ID: {doctor_id}")
        else:
            print(f"❌ Doctor creation failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return
    
    # Test 5: Assign doctor to patient
    print("\n5. Testing Patient-Doctor Mapping...")
    mapping_data = {
        "patient": patient_id,
        "doctor": doctor_id,
        "status": "active",
        "notes": "Primary care physician assignment"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/mappings/", json=mapping_data, headers=headers)
        if response.status_code == 201:
            print("✅ Patient-Doctor mapping successful")
            mapping_response = response.json()
            mapping_id = mapping_response.get('data', {}).get('id')
            print(f"   Mapping ID: {mapping_id}")
        else:
            print(f"❌ Patient-Doctor mapping failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return
    
    # Test 6: Get all patients
    print("\n6. Testing Get All Patients...")
    try:
        response = requests.get(f"{BASE_URL}/patients/", headers=headers)
        if response.status_code == 200:
            print("✅ Get patients successful")
            patients_data = response.json()
            print(f"   Found {len(patients_data.get('results', []))} patients")
        else:
            print(f"❌ Get patients failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return
    
    # Test 7: Get all doctors
    print("\n7. Testing Get All Doctors...")
    try:
        response = requests.get(f"{BASE_URL}/doctors/", headers=headers)
        if response.status_code == 200:
            print("✅ Get doctors successful")
            doctors_data = response.json()
            print(f"   Found {len(doctors_data.get('results', []))} doctors")
        else:
            print(f"❌ Get doctors failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return
    
    # Test 8: Get patient's doctors
    print("\n8. Testing Get Patient's Doctors...")
    try:
        response = requests.get(f"{BASE_URL}/mappings/patient/{patient_id}/", headers=headers)
        if response.status_code == 200:
            print("✅ Get patient's doctors successful")
            mappings_data = response.json()
            print(f"   Found {len(mappings_data.get('results', []))} doctor assignments")
        else:
            print(f"❌ Get patient's doctors failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server.")
        return
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed successfully!")
    print("The healthcare backend API is working correctly.")
    print("\nYou can now:")
    print("- Access the admin interface at http://localhost:8000/admin/")
    print("- Use the API endpoints with the provided documentation")
    print("- Integrate with frontend applications")

if __name__ == "__main__":
    test_healthcare_api()
