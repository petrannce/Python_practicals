from geopy.geocoders import Nominatim

def get_address_details(postal_code):
    geolocator = Nominatim(user_agent="address_lookup")
    try:
        location = geolocator.geocode({"postalcode": postal_code}, exactly_one=True)
        if location:
            address = location.address
            city = location.raw['address'].get('city')
            state = location.raw['address'].get('state')
            return {"address": address, "city": city, "state": state}
        else:
            return "Address not found"
    except Exception as e:
        return f"Error: {e}"
    
if __name__ == "__main__":
    postal_code = input("Enter the postal code: ")
    result = get_address_details(postal_code)
    print(result)