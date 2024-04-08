import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium

from geopy.geocoders import Nominatim

# taking input the phonenumber along with the country code
try:
    number = input("Enter the PhoneNumber with the country code : ")
    phoneNumber = phonenumbers.parse(number)

    # Using the geocoder module of phonenumbers to print the Location in console
    yourLocation = geocoder.description_for_number(phoneNumber,"en")
    print("location : "+yourLocation)

    # Using the carrier module of phonenumbers to print the service provider name in console
    yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
    print("service provider : "+yourServiceProvider)

    # Using Geopy to get the latitude and longitude of the location
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(yourLocation)

    # Handling the case when the location is not found
    if location is None:
        print("Location not found")
        exit()

    # Assigning the latitude and longitude values to the lat and lng variables
    lat = location.latitude
    lng = location.longitude

    # Getting the map for the given latitude and longitude
    myMap = folium.Map(location=[lat,lng],zoom_start = 9)

    # Adding a Marker on the map to show the location name
    folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

    # save map to html file to open it and see the actual location in map format
    myMap.save("Location.html")

except phonenumbers.phonenumberutil.NumberParseException as e:
    print("Invalid phone number format")