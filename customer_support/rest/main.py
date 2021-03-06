from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

from customer_support.rest.routers import complaints


class JWTBearer(HTTPBearer):
    httpBearer: HTTPBearer
    roles = []

    def __init__(self, roles: []):
        super(JWTBearer, self).__init__()
        self.roles = roles

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        try:
            payload = jwt.decode(credentials.credentials, "secret to test", algorithms=["HS256"])
            role: str = payload.get("role")
            if role is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non Role")
            if role not in self.roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
            return credentials
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token or expired token")


app = FastAPI(title='TPV', dependencies=[Depends(JWTBearer(["ADMIN", "MANAGER", "OPERATOR"]))])

app.include_router(complaints.router)
