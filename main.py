import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get('/')
async def main():
    return {'key': 'hello test v2'}


Instrumentator().instrument(app).expose(app, endpoint="/metrics")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
