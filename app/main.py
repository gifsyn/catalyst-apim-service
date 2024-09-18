from fastapi import FastAPI

from app.schemas.health_check import HealthCheckResponse, HealthCheckStatus
from app.settings import project_settings

app = FastAPI(
    title=project_settings.name,
    description=("Azure OpenAI Service、Amazon Bedrock、"
                 "Google Cloud Vertex AIの統合APIサービス"),
    version=project_settings.version,
)

@app.get("/", response_model = HealthCheckResponse)
async def health_check() -> HealthCheckResponse:
    """
    サーバーが起動しているか確認する.
    """

    response = HealthCheckResponse(status=HealthCheckStatus.READY)

    return response
