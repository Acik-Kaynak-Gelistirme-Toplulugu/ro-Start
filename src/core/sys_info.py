import platform
import shutil
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    import psutil
except ImportError:
    psutil = None
    logging.warning("psutil not installed. RAM info will be inaccurate.")

def get_size_str(bytes):
    """Converts bytes to human readable string."""
    for unit in ['', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if bytes < 1024:
            return f"{bytes:.1f} {unit}"
        bytes /= 1024
    return f"{bytes:.1f} PB"

def get_cpu_info():
    """Retrieves CPU model name."""
    try:
        if sys.platform == "linux":
            # Read from /proc/cpuinfo for reliability on Linux
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

        elif sys.platform == "darwin": # macOS (Development)
             command = "sysctl -n machdep.cpu.brand_string"
             return subprocess.check_output(command, shell=True).decode().strip()
             
    except Exception as e:
        logging.error(f"Error getting CPU info: {e}")
        pass
    
    return platform.processor() or "Unknown CPU"

def get_gpu_info():
    """Retrieves GPU model name."""
    try:
        if sys.platform == "linux":
            # Try lspci
            if shutil.which("lspci"):
                try:
                    # Look for VGA compatible controller
                    # Use -mm for machine readable output if possible, but standard grep is fine for now
                    cmd = r"lspci | grep -i 'vga\|3d' | cut -d: -f3 | head -n 1"
                    output = subprocess.check_output(cmd, shell=True).decode().strip()
                    if output:
                        # Clean up output (remove brackets sometimes found)
                        return output.split('[')[-1].split(']')[0] if '[' in output else output
                except subprocess.CalledProcessError:
                    pass
        elif sys.platform == "darwin":
            # macOS system profiler
             cmd = "system_profiler SPDisplaysDataType | grep 'Chipset Model' | cut -d: -f2"
             output = subprocess.check_output(cmd, shell=True).decode().strip()
             if output: return output

    except Exception as e:
        logging.error(f"Error getting GPU info: {e}")
        pass
    
    return "N/A (Driver not active)"

def get_system_specs():
    """Aggregates all system specifications."""
    try:
        # RAM
        if psutil:
            ram_bytes = psutil.virtual_memory().total
            ram_str = get_size_str(ram_bytes)
            # Add type if possible? psutil doesn't give DDR type easily.
        else:
            ram_str = "Unknown"
        
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
    except Exception as e:
        logging.error(f"Error getting system specs: {e}")
        return {
            "cpu": "Unknown",
            "gpu": "Unknown",
            "ram": "Unknown",
            "storage": "Unknown"
        }
