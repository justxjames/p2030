import subprocess
import sys

def install(package):
    """Installs a Python package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    # List of packages to install
    packages = [
        'flask',
        'requests',
        'numpy',  # Add more packages as needed
        'firebase-admin'  # Firebase Admin SDK for Python
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        install(package)
    
    print("All packages installed.")

if __name__ == "__main__":
    main()
