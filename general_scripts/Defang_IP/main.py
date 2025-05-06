
def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address

Ipad = input("Enter the IP address: ")
ipaddress = ip_address(Ipad)
print("Defanged IP address: " + ipaddress)
   