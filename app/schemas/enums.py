
from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

class ServiceOrderStatusEnum(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    CANCELED = "CANCELED"

