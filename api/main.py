import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.core.database import engine, ModelBase
from api import routers

ModelBase.metadata.create_all(bind=engine)
app = FastAPI()

# Anything with the router
for _r in routers.routes:
    app.include_router(_r)


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
