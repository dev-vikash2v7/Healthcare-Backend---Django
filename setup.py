#!/usr/bin/env python3
"""
Setup script for the Healthcare Backend System.
This script automates the installation and setup process.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def create_virtual_environment():
    """Create a virtual environment."""
    if os.path.exists("venv"):
        print("✅ Virtual environment already exists")
        return True
    
    return run_command("python -m venv venv", "Creating virtual environment")

def activate_virtual_environment():
    """Activate the virtual environment."""
    if platform.system() == "Windows":
        activate_script = "venv\\Scripts\\activate"
    else:
        activate_script = "venv/bin/activate"
    
    if not os.path.exists(activate_script):
        print("❌ Virtual environment activation script not found")
        return False
    
    print("✅ Virtual environment ready for activation")
    print(f"   To activate: {'venv\\Scripts\\activate' if platform.system() == 'Windows' else 'source venv/bin/activate'}")
    return True

def install_dependencies():
    """Install Python dependencies."""
    if platform.system() == "Windows":
        pip_cmd = "venv\\Scripts\\pip"
    else:
        pip_cmd = "venv/bin/pip"
    
    return run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies")

def create_env_file():
    """Create a .env file with default settings."""
    env_content = """DEBUG=True
SECRET_KEY=django-insecure-change-this-in-production
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
"""
    
    if os.path.exists(".env"):
        print("✅ .env file already exists")
        return True
    
    try:
        with open(".env", "w") as f:
            f.write(env_content)
        print("✅ Created .env file with default settings")
        print("   ⚠️  Please update the database credentials in .env file")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def run_migrations():
    """Run Django migrations."""
    if platform.system() == "Windows":
        python_cmd = "venv\\Scripts\\python"
    else:
        python_cmd = "venv/bin/python"
    
    success1 = run_command(f"{python_cmd} manage.py makemigrations", "Creating migrations")
    success2 = run_command(f"{python_cmd} manage.py migrate", "Running migrations")
    return success1 and success2

def create_superuser():
    """Create a superuser account."""
    print("\n👤 Superuser Creation")
    print("You can create a superuser account now or later using:")
    print("   python manage.py createsuperuser")
    
    response = input("Create superuser now? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        if platform.system() == "Windows":
            python_cmd = "venv\\Scripts\\python"
        else:
            python_cmd = "venv/bin/python"
        
        return run_command(f"{python_cmd} manage.py createsuperuser", "Creating superuser")
    else:
        print("⏭️  Skipping superuser creation")
        return True

def main():
    """Main setup function."""
    print("🏥 Healthcare Backend System Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Activate virtual environment
    if not activate_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    # Run migrations
    if not run_migrations():
        sys.exit(1)
    
    # Create superuser
    if not create_superuser():
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Update the database credentials in .env file")
    print("2. Activate the virtual environment:")
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("3. Start the development server:")
    print("   python manage.py runserver")
    print("4. Access the admin interface at http://localhost:8000/admin/")
    print("5. Test the API using the test_api.py script")
    print("\nFor detailed documentation, see README.md")

if __name__ == "__main__":
    main()
