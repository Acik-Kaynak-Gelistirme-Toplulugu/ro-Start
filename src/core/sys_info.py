import platform
import psutil
import shutil
import subprocess
import os
import sys

def get_size_str(bytes):
    for unit in ['', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} PB"

def get_cpu_info():
    try:
        if sys.platform == "linux":
            command = "cat /proc/cpuinfo | grep 'model name' | uniq | cut -d: -f2"
            output = subprocess.check_output(command, shell=True).decode().strip()
            if output:
                return output
        elif sys.platform == "darwin": # Fallback for dev environment (Mac)
             command = "sysctl -n machdep.cpu.brand_string"
             output = subprocess.check_output(command, shell=True).decode().strip()
             if output:
                 return output
    except Exception:
        pass
    return platform.processor() or "Unknown CPU"

def get_gpu_info():
    gpu_name = "Unknown GPU"
    try:
        if sys.platform == "linux":
            # Try lspci
            try:
                # Look for VGA compatible controller
                cmd = r"lspci | grep -i 'vga\|3d' | cut -d: -f3 | head -n 1"
                output = subprocess.check_output(cmd, shell=True).decode().strip()
                if output:
                    return output
            except:
                pass
    except Exception:
        pass
    
    # Fallback to a generic text if we can't find it easily without external deps like pciutils
    return "N/A (Driver not active)"

def get_system_specs():
    # RAM
    ram_bytes = psutil.virtual_memory().total
    ram_str = get_size_str(ram_bytes).replace(" ", " ") # Ensure formatting
    
    # Storage (Root partition)
    total, used, free = shutil.disk_usage("/")
    storage_str = get_size_str(total)
    
    cpu_name = get_cpu_info()
    gpu_name = get_gpu_info()
    
    return {
        "cpu": cpu_name,
        "gpu": gpu_name,
        "ram": ram_str,
        "storage": storage_str
    }
