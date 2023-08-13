from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import employee

app = FastAPI()

# Accept CORS Error to run app locally.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Vue.js server's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee.router)


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
