# Healthcare Backend System

A comprehensive Django REST Framework backend system for healthcare management with JWT authentication, patient and doctor management, and patient-doctor mapping functionality.

## Features

- **JWT Authentication**: Secure user registration and login with JWT tokens
- **Patient Management**: Complete CRUD operations for patient records
- **Doctor Management**: Complete CRUD operations for doctor records
- **Patient-Doctor Mapping**: Assign doctors to patients and manage relationships
- **PostgreSQL Database**: Robust database backend
- **RESTful API**: Clean and consistent API endpoints
- **Admin Interface**: Django admin for data management
- **Error Handling**: Comprehensive error handling and validation

## Technology Stack

- **Django 4.2.7**: Web framework
- **Django REST Framework 3.14.0**: API framework
- **djangorestframework-simplejwt 5.3.0**: JWT authentication
- **PostgreSQL**: Database

## Installation and Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### 1. Clone the Repository

```bash
git clone <repository-url>
cd healthcare-backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE healthcare_db;
CREATE USER healthcare_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO healthcare_user;
```

### 5. Environment Configuration

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Server

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

## API Endpoints

### Authentication

#### Register User
```
POST /api/auth/register/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "secure_password123",
    "password2": "secure_password123",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

#### Login User
```
POST /api/auth/login/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "secure_password123"
}
```

Response:
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

#### Refresh Token
```
POST /api/auth/token/refresh/
Content-Type: application/json

{
    "refresh": "your_refresh_token_here"
}
```

#### Get User Profile
```
GET /api/auth/profile/
Authorization: Bearer your_access_token_here
```

### Patient Management

#### Create Patient
```
POST /api/patients/
Authorization: Bearer your_access_token_here
Content-Type: application/json

{
    "first_name": "Jane",
    "last_name": "Smith",
    "date_of_birth": "1990-05-15",
    "gender": "F",
    "blood_group": "A+",
    "phone_number": "+1234567890",
    "email": "jane@example.com",
    "address": "123 Main St, City, State 12345",
    "emergency_contact_name": "John Smith",
    "emergency_contact_phone": "+1234567891",
    "medical_history": "No significant medical history",
    "allergies": "None",
    "current_medications": "None",
    "insurance_provider": "Blue Cross",
    "insurance_number": "BC123456789"
}
```

#### Get All Patients (for authenticated user)
```
GET /api/patients/
Authorization: Bearer your_access_token_here
```

#### Get Patient Details
```
GET /api/patients/{id}/
Authorization: Bearer your_access_token_here
```

#### Update Patient
```
PUT /api/patients/{id}/
Authorization: Bearer your_access_token_here
Content-Type: application/json

{
    "first_name": "Jane",
    "last_name": "Smith",
    "phone_number": "+1234567890",
    "email": "jane.updated@example.com"
}
```

#### Delete Patient
```
DELETE /api/patients/{id}/
Authorization: Bearer your_access_token_here
```

### Doctor Management

#### Create Doctor
```
POST /api/doctors/
Authorization: Bearer your_access_token_here
Content-Type: application/json

{
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
    "is_available": true
}
```

#### Get All Doctors
```
GET /api/doctors/
Authorization: Bearer your_access_token_here
```

#### Get Doctor Details
```
GET /api/doctors/{id}/
Authorization: Bearer your_access_token_here
```

#### Update Doctor
```
PUT /api/doctors/{id}/
Authorization: Bearer your_access_token_here
Content-Type: application/json

{
    "consultation_fee": 175.00,
    "is_available": false
}
```

#### Delete Doctor
```
DELETE /api/doctors/{id}/
Authorization: Bearer your_access_token_here
```

### Patient-Doctor Mapping

#### Assign Doctor to Patient
```
POST /api/mappings/
Authorization: Bearer your_access_token_here
Content-Type: application/json

{
    "patient": 1,
    "doctor": 1,
    "status": "active",
    "notes": "Primary care physician assignment"
}
```

#### Get All Mappings
```
GET /api/mappings/
Authorization: Bearer your_access_token_here
```

#### Get Doctors for Specific Patient
```
GET /api/mappings/patient/{patient_id}/
Authorization: Bearer your_access_token_here
```

#### Update Mapping
```
PUT /api/mappings/{id}/
Authorization: Bearer your_access_token_here
Content-Type: application/json

{
    "status": "inactive",
    "notes": "Patient transferred to different doctor"
}
```

#### Remove Doctor from Patient
```
DELETE /api/mappings/{id}/
Authorization: Bearer your_access_token_here
```

## Database Models

### UserProfile
- Extends Django's User model with additional fields
- Phone number, address, date of birth
- Automatically created when a user is registered

### Patient
- Comprehensive patient information
- Medical history, allergies, medications
- Insurance information
- Emergency contact details
- Created by authenticated users

### Doctor
- Professional information and credentials
- Specialization and experience
- Contact and availability information
- License and certification details

### PatientDoctorMapping
- Links patients to doctors
- Assignment status and notes
- Tracks who made the assignment
- Prevents duplicate assignments

## Security Features

- JWT token-based authentication
- Password validation and hashing
- CORS configuration for frontend integration
- Environment variable management for sensitive data
- User-specific data access (patients are filtered by creator)

## Error Handling

The API provides comprehensive error handling:

- Validation errors with detailed field-specific messages
- Authentication and permission errors
- Database constraint violations
- Proper HTTP status codes

## Admin Interface

Access the Django admin interface at `http://localhost:8000/admin/` to:

- Manage users and user profiles
- View and edit patient records
- Manage doctor information
- Handle patient-doctor mappings
- Monitor system activity

## Testing

To run tests:

```bash
python manage.py test
```

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Use a strong `SECRET_KEY`
3. Configure proper database credentials
4. Set up proper CORS origins
5. Use HTTPS
6. Configure static file serving
7. Set up proper logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License.
