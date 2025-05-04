import wmi

data = wmi.WMI()
for os in data.Win32_OperatingSystem():
    print(f"Version: {os.Version}")
    print(f"Build Number: {os.BuildNumber}")
    print(f"OS Name: {os.Name}")
    print(f"Manufacturer: {os.Manufacturer}")
    print(f"Serial Number: {os.SerialNumber}")
    print(f"System Directory: {os.SystemDirectory}")
    print(f"Windows Directory: {os.WindowsDirectory}")
    print(f"Last Boot Up Time: {os.LastBootUpTime}")
    print(f"Total Visible Memory Size: {os.TotalVisibleMemorySize}")
    print(f"Free Physical Memory: {os.FreePhysicalMemory}")
    print(f"Total Virtual Memory Size: {os.TotalVirtualMemorySize}")
    print(f"Free Virtual Memory: {os.FreeVirtualMemory}")
    print(f"Number of Processes: {os.NumberOfProcesses}")  # Example of additional property
    print(f"Number of Users: {os.NumberOfUsers}")  # Example of additional property
    print(f"OS Architecture: {os.OSArchitecture}")  # Example of additional property
    print(f"Country Code: {os.CountryCode}")  # Example of additional property
    print(f"Locale: {os.Locale}")  # Example of additional property
    print(f"Boot Device: {os.BootDevice}")  # Example of additional property
    print(f"System Name: {os.SystemDrive}")  # Example of additional property
