from fastapi import FastAPI

from app.api.routers import routers
from app.core.settings import project_settings

app = FastAPI(
    title=project_settings.name,
    description="Azure OpenAI Service、Amazon Bedrock、Google Cloud Vertex AIの統合APIサービス",
    version=project_settings.version,
)

app.include_router(routers)
