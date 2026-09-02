import platform
import psutil


def get_system_info():
    return {
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "cpu_count": psutil.cpu_count(),
        "memory_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2)
    }


def get_memory_info():
    memory = psutil.virtual_memory()

    return {
        "total_gb": round(memory.total / (1024 ** 3), 2),
        "available_gb": round(memory.available / (1024 ** 3), 2),
        "used_gb": round(memory.used / (1024 ** 3), 2),
        "usage_percent": memory.percent
    }


def get_disk_info():
    disk = psutil.disk_usage("C:\\")

    return {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
        "usage_percent": disk.percent
    }
def get_cpu_info():
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "cpu_count": psutil.cpu_count()
    }