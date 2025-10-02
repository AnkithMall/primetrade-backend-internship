from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

# Limiter initialized with remote IP
limiter = Limiter(key_func=get_remote_address)

def get_rate_limit_headers(request: Request):
    return {
        "X-RateLimit-Limit": request.state.view_rate_limit.limit,
        "X-RateLimit-Remaining": request.state.view_rate_limit.remaining,
        "X-RateLimit-Reset": request.state.view_rate_limit.reset,
    }
