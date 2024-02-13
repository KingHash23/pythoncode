from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="geoapiExercises")

def get_location_by_address(address):
    """This function returns a location as raw from an address
    will repeat until success"""
    time.sleep(1)
    try:
        return geolocator.geocode(address).raw
    except:
        return get_location_by_address(address)

def get_address_by_location(latitude, longitude, language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    coordinates = f"{latitude}, {longitude}"
    time.sleep(1)
    try:
        return geolocator.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)

address = "Makai Road, Masaki, Dar es Salaam, Tanzania"
location = get_location_by_address(address)
print(f"Latitude: {location['lat']}, Longitude: {location['lon']}")

latitude = 36.723
longitude = 3.188
address = get_address_by_location(latitude, longitude)
print(f"Address: {address['display_name']}") 