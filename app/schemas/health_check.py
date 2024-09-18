from enum import Enum

from pydantic import BaseModel


class HealthCheckStatus(Enum):
    READY = "ready"


class HealthCheckResponse(BaseModel):
    status: HealthCheckStatus = HealthCheckStatus.READY
