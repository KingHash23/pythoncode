from phonenumbers import geocoder

# Take the phone number as input
number = input("Enter the phone number with country code: ")

# Parse the phone number
phone_number = geocoder.find_format(number, "International")

# Print the country of the phone number
print(f"The phone number is from: {phone_number.country_name}")

# Print the geolocation of the phone number
print(f"The geolocation of the phone number is: {geocoder.description_for_number(phone_number, 'en')}")