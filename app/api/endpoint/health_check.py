from fastapi import APIRouter

from app.api.schema.health_check import HealthCheckResponse

router = APIRouter()


@router.get("/", response_model=HealthCheckResponse)
async def health_check() -> HealthCheckResponse:
    """Health Check API."""
    return HealthCheckResponse()
