from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

# Routers will be added here
# from .routers import customer, admin, sse
# app.include_router(customer.router, prefix="/api/customer", tags=["Customer"])
# app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
# app.include_router(sse.router, prefix="/api/sse", tags=["SSE"])
