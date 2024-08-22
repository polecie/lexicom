from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.api import router
from src.conf import conf
from src.db import redis

conf = conf()


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis_instance = await redis.RedisServer.connect()
    yield
    await app.state.redis_instance.close()


app = FastAPI(lifespan=lifespan, debug=conf.api.debug)

app.include_router(router)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=conf.api.host, port=conf.api.port)
