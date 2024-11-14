from fastapi import APIRouter

from app.api.endpoint import azure_openai_service, health_check

routers = APIRouter()

routers.include_router(health_check.router, tags=["Health Check"])
