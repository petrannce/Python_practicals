import os
import subprocess

def flush_dns():
    """Flush DNS cache to improve network performance"""
    os.system("ipconfig /flushdns")

def restart_network():
    """Restart network adapter"""
    os.system("ipconfig /release && ipconfig /renew")

def set_faster_dns():
    """Set Google DNS (8.8.8.8, 8.8.4.4)"""
    os.system('netsh interface ip set dns name="Wi-Fi" static 8.8.8.8')
    os.system('netsh interface ip add dns name="Wi-Fi" 8.8.4.4 index=2')

def close_bandwidth_hogging_apps():
    """Kill apps consuming bandwidth"""
    apps_to_kill = ["chrome.exe", "steam.exe", "onedrive.exe", "utorrent.exe"]
    for app in apps_to_kill:
        subprocess.run(["taskkill", "/F", "/IM", app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def optimize_network():
    """Run all optimizations"""
    print("Flushing DNS cache...")
    flush_dns()
    
    print("Setting Google DNS...")
    set_faster_dns()
    
    print("Restarting network...")
    restart_network()
    
    print("Closing bandwidth-heavy apps...")
    close_bandwidth_hogging_apps()
    
    print("✅ Network optimization complete! Try running a speed test.")

if __name__ == "__main__":
    optimize_network()
