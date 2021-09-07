import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import routers
from api.core.config import settings

app = FastAPI()

# Anything with the router v1
for _r in routers.v1_routes:
    app.include_router(_r, prefix=settings.V1_API_PREFIX)


# Register all the middlewares here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
def read_root():
    return {"Health": "OK!"}


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, access_log=True)
