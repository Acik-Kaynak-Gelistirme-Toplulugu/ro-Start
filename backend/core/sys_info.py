import platform
import shutil
import subprocess
import sys
import logging
import os
from functools import lru_cache

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    import psutil
except ImportError:
    psutil = None
    logging.warning("psutil not installed. RAM info will be inaccurate.")


def get_size_str(size_bytes):
    """Converts bytes to human readable string."""
    for unit in ["", "KB", "MB", "GB", "TB", "PB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"


@lru_cache(maxsize=1)
def get_cpu_info():
    """Retrieves CPU model name. Cached."""
    try:
        if sys.platform == "linux":
            # Read from /proc/cpuinfo for reliability on Linux - much faster than lscpu
            try:
                with open("/proc/cpuinfo", "r") as f:
                    for line in f:
                        if "model name" in line:
                            return line.split(":")[1].strip()
            except FileNotFoundError:
                pass

            # Fallback to lscpu if /proc/cpuinfo fails
            if shutil.which("lscpu"):
                cmd = "lscpu | grep 'Model name' | cut -d: -f2"
                return subprocess.check_output(cmd, shell=True).decode().strip()

        elif sys.platform == "darwin":  # macOS
            # sysctl is reasonably fast
            command = "sysctl -n machdep.cpu.brand_string"
            return subprocess.check_output(command, shell=True).decode().strip()

    except Exception as e:
        logging.error(f"Error getting CPU info: {e}")
        pass

    return platform.processor() or "Unknown CPU"


@lru_cache(maxsize=1)
def get_gpu_info():
    """Retrieves GPU model name. Cached."""
    try:
        if sys.platform == "linux":
            # Try lspci
            if shutil.which("lspci"):
                try:
                    # Look for VGA compatible controller
                    cmd = r"lspci | grep -i 'vga\|3d' | cut -d: -f3 | head -n 1"
                    output = subprocess.check_output(cmd, shell=True).decode().strip()
                    if output:
                        return output.split("[")[-1].split("]")[0] if "[" in output else output
                except subprocess.CalledProcessError:
                    pass
        elif sys.platform == "darwin":
            # macOS system profiler is slow, but we cache it now.
            # Using grep to limit output parsing
            cmd = "system_profiler SPDisplaysDataType | grep 'Chipset Model' | cut -d: -f2"
            output = subprocess.check_output(cmd, shell=True).decode().strip()
            if output:
                return output

    except Exception as e:
        logging.error(f"Error getting GPU info: {e}")
        pass

    return "N/A (Driver not active)"


def get_distro_info():
    """Retrieves distribution name, version, and ID."""
    distro_name = "Linux"
    distro_version = "Unknown"
    distro_id = "linux"

    try:
        if sys.platform == "linux":
            if os.path.exists("/etc/os-release"):
                with open("/etc/os-release") as f:
                    data = {}
                    for line in f:
                        if "=" in line:
                            k, v = line.strip().split("=", 1)
                            data[k] = v.strip('"')

                    if "NAME" in data:
                        distro_name = data["NAME"]
                    if "VERSION_ID" in data:
                        distro_version = data["VERSION_ID"]
                    if "ID" in data:
                        distro_id = data["ID"]

        elif sys.platform == "darwin":
            distro_name = "macOS"
            distro_version = platform.mac_ver()[0]
            distro_id = "macos"

    except Exception as e:
        logging.error(f"Error getting distro info: {e}")
        pass

    return distro_name, distro_version, distro_id


def get_system_specs():
    """Aggregates all system specifications."""
    try:
        # RAM
        if psutil:
            ram_bytes = psutil.virtual_memory().total
            ram_str = get_size_str(ram_bytes)
        else:
            ram_str = "Unknown"

        # Storage (Root partition)
        total, used, free = shutil.disk_usage("/")
        storage_str = get_size_str(total)

        cpu_name = get_cpu_info()
        gpu_name = get_gpu_info()
        distro_name, distro_version, distro_id = get_distro_info()

        return {
            "cpu": cpu_name,
            "gpu": gpu_name,
            "ram": ram_str,
            "storage": storage_str,
            "distro": distro_name,
            "version": distro_version,
            "distro_id": distro_id,
        }
    except Exception as e:
        logging.error(f"Error getting system specs: {e}")
        return {
            "cpu": "Unknown",
            "gpu": "Unknown",
            "ram": "Unknown",
            "storage": "Unknown",
            "distro": "Linux",
            "version": "Unknown",
        }
