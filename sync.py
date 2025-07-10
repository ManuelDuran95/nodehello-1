import google.auth.transport.requests
from google.auth.credentials import IDTokenCredentials

def generate_auth_token(audience: str, target_principal: str):
    """Generate Auth token needed to call API hosted on Cloud Run
    Args:
    audience: (str) Url of Cloud Run where auth is needed
    target_prinicipal: (str) Service account to impersonate
    Returns:
    Auth Identity token
    """
    scopes = ['https://www.googleapis.com/auth/cloud-platform']
    request = google.auth.transport.requests.Request()
    creds, _ = google.auth.default(scopes=scopes)
    icreds = google.auth.impersonated_credentials.Credentials(
        source_credentials=creds,
        target_principal=target_principal,
        target_scopes=scopes)
    id = IDTokenCredentials(icreds, target_audience=audience,include_email=True)
    id.refresh(request)
    return id.token

