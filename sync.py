from google.auth.impersonated_credentials import IDTokenCredentials
import google.auth
import google.auth.transport.requests
from google.auth import credentials
from google.oauth2 import service_account
import requests
import json

def generate_auth_token(audience: str, target_principal: str):
    """Generate Auth token needed to call API hosted on Cloud Run
    Args:
    audience: (str) Url of Cloud Run where auth is needed
    target_prinicipal: (str) Service account to impersonate
    Returns:
    Auth Identity token
    """
    print(audience)
    print(target_principal)
 
    scopes = ['https://www.googleapis.com/auth/cloud-platform']
    request = google.auth.transport.requests.Request()
    creds, _ = google.auth.default(scopes=scopes)
    icreds = google.auth.impersonated_credentials.Credentials(
        source_credentials=creds,
        target_principal=target_principal,
        target_scopes=scopes)
    id = IDTokenCredentials(icreds, target_audience=audience,include_email=True)
    id.refresh(request)
    print(id.token)
    toke=id.token
    headers = {
        'Authorization': f'Bearer {toke}'
    }
    response = requests.get('https://python-test34-95436488673.europe-west1.run.app', headers=headers)
    response.raise_for_status()
    # Print the status code
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(data)
    return id.token
audience="https://python-test34-95436488673.europe-west1.run.app"
sa1="test112024@manuelmata-dev.iam.gserviceaccount.com"
generate_auth_token(audience,sa1)
