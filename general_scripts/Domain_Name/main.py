import whois

def get_domain_info(domain_name):

    try:
        domain_info = whois.whois(domain_name)
        print(f"Domain Name:", {domain_info.domain_name})
        print(f"Registrar:", {domain_info.registrar})
        print(f"Creation Date:", {domain_info.creation_date})
        print(f"Expiration Date:", {domain_info.expiration_date})
        print(f"Name Servers:", {domain_info.name_servers})
        print(f"Status:", {domain_info.status})
        print(domain_info)

    except Exception as e:
        print(f"Error retrieving information: {e}")

if __name__ == "__main__":
    domain_name = input("Enter a domain name (e.g., example.com): ")
    get_domain_info(domain_name)