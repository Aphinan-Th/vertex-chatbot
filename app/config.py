import os

GOOGLE_CLOUD_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT_ID", "")
GOOGLE_CLOUD_REGION = os.getenv("GOOGLE_CLOUD_REGION", "us-central1")
GOOGLE_CLOUD_DATA_STORE_REGION = os.getenv("GOOGLE_CLOUD_DATA_STORE_REGION", "global")
GOOGLE_SERVICE_ACCOUNT_CREDENTIAL_PATH = os.getenv(
    "GOOGLE_SERVICE_ACCOUNT_CREDENTIAL_PATH", "./credentials/gcp.json"
)
ALL_PRODUCTS = os.getenv("ALL_PRODUCTS", "")
DEFAULT_TEMPERATURE = 0.0
GEMINI_MODEL = "gemini-2.0-pro-exp-02-05"
