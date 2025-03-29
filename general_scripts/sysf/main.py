import platform
import psutil
import subprocess

def get_system_specs():
    system = platform.system()
    brand = "Unknown"
    
    # Get brand/manufacturer
    if system == "Windows":
        try:
            brand = subprocess.check_output("wmic computersystem get manufacturer", shell=True).decode().split("\n")[1].strip()
        except Exception:
            pass
    elif system == "Darwin":  # macOS
        try:
            brand = subprocess.check_output(["system_profiler", "SPHardwareDataType"]).decode()
            for line in brand.split("\n"):
                if "Model Name" in line:
                    brand = line.split(": ")[-1].strip()
                    break
        except Exception:
            pass
    elif system == "Linux":
        try:
            brand = subprocess.check_output("cat /sys/devices/virtual/dmi/id/product_name", shell=True).decode().strip()
        except Exception:
            pass
    
    # Get CPU details
    processor = platform.processor()
    
    # Get RAM size in GB
    ram = round(psutil.virtual_memory().total / (1024 ** 3))
    
    return f"Brand Name: {brand},\n Processor details: {processor}, \n RAM: {ram} GB"

if __name__ == "__main__":
    print(get_system_specs())
