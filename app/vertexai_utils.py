import vertexai
from config import (
    DEFAULT_TEMPERATURE,
    GEMINI_MODEL,
    GOOGLE_CLOUD_PROJECT_ID,
    GOOGLE_CLOUD_REGION,
    GOOGLE_SERVICE_ACCOUNT_CREDENTIAL_PATH,
)
from google.oauth2.service_account import Credentials
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
)


def init_vertexai():
    vertexai.init(
        project=GOOGLE_CLOUD_PROJECT_ID,
        location=GOOGLE_CLOUD_REGION,
        credentials=Credentials.from_service_account_file(
            GOOGLE_SERVICE_ACCOUNT_CREDENTIAL_PATH
        ),
    )


def init_model(system_instruction="You are a helpful AI assistant."):
    config = GenerationConfig(
        max_output_tokens=8000,
        temperature=DEFAULT_TEMPERATURE,
    )

    return GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=[system_instruction],
        generation_config=config,
    )
