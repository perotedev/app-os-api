
import enum

class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    USER = "USER"

class ServiceOrderStatusEnum(str, enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    CANCELED = "CANCELED"

