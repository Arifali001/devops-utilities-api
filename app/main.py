from fastapi import FastAPI
from app.utils import get_system_info, get_memory_info, get_disk_info, get_cpu_info

app = FastAPI(
    title="DevOps Utilities API",
    description="DevOps utility API built with Python and FastAPI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "DevOps Utilities API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/system")
def system_info():
    return get_system_info()


@app.get("/memory")
def memory_info():
    return get_memory_info()


@app.get("/disk")
def disk_info():
    return get_disk_info()

@app.get("/cpu")
def cpu_info():
    return get_cpu_info()