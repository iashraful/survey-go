import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.survey import routers as survey_routers
from api.auth import routers as auth_routers
from api.core.config import settings

app = FastAPI(title='Survey Go API Documentation')

# Auth Module APIs
for _r in auth_routers.v1_routes:
    app.include_router(_r, prefix=settings.V1_API_PREFIX)

for _r in auth_routers.v2_routes:
    app.include_router(_r, prefix=settings.V2_API_PREFIX)

# SURVEY Module APIs
for _r in survey_routers.v1_routes:
    app.include_router(_r, prefix=settings.V1_API_PREFIX)

for _r in survey_routers.v2_routes:
    app.include_router(_r, prefix=settings.V2_API_PREFIX)

# Register all the middlewares here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# @app.on_event('startup')
# async def startup():
#     app.add_middleware(AuthenticationMiddleware, backend=BearerTokenAuthBackend())


@app.get("/")
def read_root():
    return {"Health": "OK!"}


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, access_log=True)
