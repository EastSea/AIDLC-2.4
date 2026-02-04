from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.customer import customer_router
from app.routers.admin import admin_router

app = FastAPI(title="Table Order API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(customer_router)
app.include_router(admin_router)
