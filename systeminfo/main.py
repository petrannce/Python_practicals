import wmi

c = wmi.WMI()

for os in c.Win32_OperatingSystem():
    print(f"OS Name: {os.Name}")
    print(f"Version: {os.Version}")
    print(f"Architecture: {os.OSArchitecture}")
    print(f"Manufacturer: {os.Manufacturer}")
    print(f"Registered User: {os.RegisteredUser}")
    print(f"Serial Number: {os.SerialNumber}")
    print(f"Number of Users: {os.NumberOfUsers}")
    print(f"Last Boot Up Time: {os.LastBootUpTime}")
    print(f"System Directory: {os.SystemDirectory}")
    print(f"System Drive: {os.SystemDrive}")
    print(f"Windows Directory: {os.WindowsDirectory}")
