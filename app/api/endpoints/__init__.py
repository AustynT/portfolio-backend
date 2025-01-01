from app.api.endpoints.users import router as users_router

from app.api.endpoints.auth import router as auth_router
# Combine all routers in a list for easier imports
routers = [
    {"router": users_router, "prefix": "/api/v1", "tags": ["users"]},
    {"router": auth_router, "prefix": "/api/v1", "tags": ["auth"]},
]
