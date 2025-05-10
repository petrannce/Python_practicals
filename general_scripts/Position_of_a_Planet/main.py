from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time

now = Time.now()

location = EarthLocation.of_site('greenwich')

planet_name = input("Enter the name of the planet (e.g., 'mars', 'jupiter'): ").strip().lower()

planet_position = get_body(planet_name, now, location)

print(f"The position of {planet_name.capitalize()} at {now.iso} is:")
print(f"RA: {planet_position.ra:.2f}, Dec: {planet_position.dec:.2f}")