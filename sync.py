from google.auth.impersonated_credentials import IDTokenCredentials
import google.auth
import google.auth.transport.requests
from google.auth import credentials
from google.oauth2 import service_account
import os
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
    print( os.environ['TOKEN'])
    scopes = ['https://www.googleapis.com/auth/cloud-platform']
    source_credentials1 = (
    service_account.Credentials.from_service_account_file(
        '${{ secrets.GCP_SA_KEY }}',
        scopes=scopes))
    request = google.auth.transport.requests.Request()
    creds, _ = google.auth.default(scopes=scopes)
    icreds = google.auth.impersonated_credentials.Credentials(
        source_credentials=source_credentials1,
        target_principal=target_principal,
        target_scopes=scopes)
    id = IDTokenCredentials(icreds, target_audience=audience,include_email=True)
    id.refresh(request)
    print(id.token)
    return id.token

token = generate_auth_token("test","test112024@manuelmata-dev.iam.gserviceaccount.com")

