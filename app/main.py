from dotenv import load_dotenv
from fastapi import FastAPI

from app.api import azure_openai_service
from app.schemas.health_check import HealthCheckResponse

load_dotenv()

app = FastAPI(
    title="Catalyst APIM Service",
    description=("Azure OpenAI Service、Amazon Bedrock、"
                 "Google Cloud Vertex AIの統合APIサービス"),
    version="0.0.0"
)

@app.get("/", response_model=HealthCheckResponse)
async def health_check() -> HealthCheckResponse:
    """サーバーが起動しているか確認する."""
    response = HealthCheckResponse()

    return response
