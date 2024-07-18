from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    Status: str = "ready"
