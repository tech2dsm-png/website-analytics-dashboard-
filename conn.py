import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import json

def test_bigquery_connection():
    """
    Connects to BigQuery, runs a test query, and prints the results.
    This script assumes you have a service account key file for authentication.
    
    Instructions:
    1. Replace the 'path/to/your/service-account.json' with the actual path to your service account key file.
    2. Replace 'your-gcp-project-id' with your Google Cloud Project ID.
    3. Replace 'your-ga4-dataset' with the name of your GA4 dataset in BigQuery.
    
    If successful, it will print the first 5 rows of your GA4 data.
    """
    
    # --- Authentication Setup ---
    # Method 1: Use a service account key file (recommended for local development)
    # Be sure to keep this file secure and outside of version control.
    try:
        # REPLACE THIS LINE with the full path to your service account key file
        # If the key file is in the same folder as this script, you can use just the filename.
        credentials_path = "service-account.json" 
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
    except FileNotFoundError:
        print(f"Error: The service account key file was not found at {credentials_path}")
        return
    except Exception as e:
        print(f"An error occurred during authentication: {e}")
        return

    # --- BigQuery Client Initialization ---
    try:
        project_id = "brilliant-dryad-439810-q6" # Replaced with your GCP project ID
        bq_client = bigquery.Client(credentials=credentials, project=project_id)
        print("Successfully authenticated and created BigQuery client.")
    except Exception as e:
        print(f"Failed to initialize BigQuery client: {e}")
        return

    # --- Test Query ---
    # This query will select the first 5 rows of your raw GA4 event data.
    # It's a great way to test the connection and preview your data's structure.
    # Replace the table name with your actual GA4 events table.
    dataset_id = "analytics_453034732" # Replaced with your BigQuery dataset ID
    table_id = f"{dataset_id}.events_*" # The wildcard '*' is for partitioned tables
    
if __name__ == "__main__":
    test_bigquery_connection()
