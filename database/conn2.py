import os
import sys
from google.cloud import bigquery
from google.oauth2 import service_account

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up one directory to find the service account key in the project root
# This makes your code robust and location-independent
key_file_path = os.path.join(script_dir, '..', 'service-account.json')

# --- FOR DEBUGGING ---
# This line will show you the exact path the script is looking for.
print(f"DEBUG: Looking for service account file at: {key_file_path}")
# --- END DEBUG ---

project_id = "brilliant-dryad-439810-q6"

try:
    credentials = service_account.Credentials.from_service_account_file(key_file_path)
    bq_client = bigquery.Client(credentials=credentials, project=project_id)
    print("[conn.py] BigQuery client initialized successfully.")
except FileNotFoundError:
    print(f"[conn.py] ERROR: Service account file not found at: {key_file_path}")
    bq_client = None
except Exception as e:
    print(f"[conn.py] ERROR: Failed to initialize BigQuery client: {e}")
    bq_client = None

# A simple function to return the client
def get_bq_client():
    return bq_client
