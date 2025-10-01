
from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, persons, addresses, clients, contracts, documents, service_types, service_orders

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(persons.router, prefix="/persons", tags=["persons"])
api_router.include_router(addresses.router, prefix="/addresses", tags=["addresses"])
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(contracts.router, prefix="/contracts", tags=["contracts"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(service_types.router, prefix="/service-types", tags=["service types"])
api_router.include_router(service_orders.router, prefix="/service-orders", tags=["service orders"])

