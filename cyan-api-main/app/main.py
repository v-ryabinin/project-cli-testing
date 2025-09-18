import uvicorn

from fastapi import FastAPI

from app.api.record import RecordRouter


recordRouter = RecordRouter()

app = FastAPI()
app.include_router(recordRouter.router, prefix="/record", tags=["record"])


if __name__ == "__main__":
    uvicorn.run("app.main:app")
