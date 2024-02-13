import geopy
from openlocationcode import OpenLocationCode

# Set up the geolocation service
geolocator = geopy.Nominatim(user_agent="geoapiExercises")

# Get the current location (latitude and longitude)
def get_location():
    try:
        location = geolocator.geocode("my location")
        return (location.latitude, location.longitude)
    except:
        return None

current_location = get_location()

if current_location:
    olc = OpenLocationCode(current_location[0], current_location[1])
    plus_code = olc.get_short_code()
    print(f"Your location's plus code is: {plus_code}")
else:
    print("Could not retrieve your location")