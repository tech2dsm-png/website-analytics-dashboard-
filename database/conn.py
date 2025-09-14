import os
import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account

bq_client = None  # always define upfront

# --- Step 1: Try local JSON (for local dev)
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, '..', 'service-account.json')
project_id = "brilliant-dryad-439810-q6"

if os.path.exists(json_path):
    try:
        credentials = service_account.Credentials.from_service_account_file(json_path)
        bq_client = bigquery.Client(credentials=credentials, project=project_id)
        print(f"[conn.py] ✅ BigQuery client initialized from local JSON: {json_path}")
    except Exception as e:
        print(f"[conn.py] ❌ Failed to init BigQuery from JSON: {e}")

# --- Step 2: If JSON not found, try Streamlit secrets (for cloud)
if bq_client is None:
    try:
        service_account_info = st.secrets.get("gcp_service_account")
        if service_account_info:
            credentials = service_account.Credentials.from_service_account_info(service_account_info)
            project_id = service_account_info.get("project_id")
            bq_client = bigquery.Client(credentials=credentials, project=project_id)
            print("[conn.py] ✅ BigQuery client initialized from Streamlit secrets")
        else:
            print("[conn.py] ⚠️ gcp_service_account not found in st.secrets")
    except Exception as e:
        print(f"[conn.py] ❌ Failed to init BigQuery from Streamlit secrets: {e}")

# --- Step 3: Function to return client
def get_bq_client():
    if bq_client is None:
        print("[conn.py] ⚠️ bq_client is None. Check your JSON or Streamlit secrets.")
    return bq_client