import os
import sys

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the Flask app
flask_app_path = os.path.join(current_dir, "app", "app.py")

# Set the environment variables
os.environ["FLASK_APP"] = flask_app_path
os.environ["FLASK_ENV"] = "development"  # Optional, for development mode

# Run the Flask app
os.system(f"{sys.executable} -m flask run")
