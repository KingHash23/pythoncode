import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium

from opencage.geocoder import OpenCageGeocode

# taking input the phonenumber along with the country code
try:
    number = input("Enter the PhoneNumber with the country code : ")
    phoneNumber = phonenumbers.parse(number)

    # Storing the API Key in the Key variable
    Key = "your_api_key_here" #generate your api from https://opencagedata.com/api

    # Using the geocoder module of phonenumbers to print the Location in console
    yourLocation = geocoder.description_for_number(phoneNumber,"en")
    print("location : "+yourLocation)

    # Using the carrier module of phonenumbers to print the service provider name in console
    yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
    print("service provider : "+yourServiceProvider)

    # Using opencage to get the latitude and longitude of the location
    geocoder = OpenCageGeocode(Key)
    query = str(yourLocation)
    results = geocoder.geocode(query)

    # Handling the case when the location is not found
    if len(results) == 0:
        print("Location not found")
        exit()

    # Assigning the latitude and longitude values to the lat and lng variables
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    # Getting the map for the given latitude and longitude
    myMap = folium.Map(location=[lat,lng],zoom_start = 9)

    # Adding a Marker on the map to show the location name
    folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

    # save map to html file to open it and see the actual location in map format
    myMap.save("Location.html")

except phonenumbers.phonenumberutil.NumberParseException as e:
    print("Invalid phone number format")