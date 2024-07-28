import importlib.util
import os
import sys

# Add the directory containing app.py to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Load the app.py module
spec = importlib.util.spec_from_file_location('app', 'app.py')
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)

# Set the WSGI application callable to the app instance from app.py
application = app_module.app
