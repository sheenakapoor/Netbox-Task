"""Python script for Netbox Internship Coding Task."""


# Importing Libraries
import requests

# Taking input from user for Zip Code, displaying it
zipcode = input("User's US Post Office ZIP Code: ")
print(f"ZIP Code: {zipcode} \n")

# Generating URL based on User's Postal ZIP Code
url = "http://wttr.in/" + zipcode

# Checking for valid Zip Code

# Generating URL with data of valid US Postal ZIP codes
checkURL = "http://www.zip-codes.com/zip-code/" + zipcode
status_code = requests.get(checkURL).status_code

# Test for validity of user's ZIP code
if status_code == 404:
    print("Invalid Zip Code, Try again")
    exit()

# Converting to JSON
params = (("format", "j1"),)
response = requests.get(url, params=params).json()

"""Getting the Current Temperature, Feels-Like Temperature, and
Weather Description for user's ZIP Code"""


# Assigning current condition key to a variable and indexing it
current_condition = response["current_condition"][0]

# Assigning variables and indexing to get Current Temperature,
# Feels-Like Temperature and Weather Description for user's ZIP Code
temp_F = current_condition["temp_F"]
FeelsLikeF = current_condition["FeelsLikeF"]
weatherDesc = current_condition["weatherDesc"][0]["value"]

# Displaying weather conditions with temperatures in Fahrenheit
print(
    f"""The weather conditions in your location are displayed below:
    Current Temperature: {temp_F}°F
    Feels like Temperature: {FeelsLikeF}°F
    Weather Description: {weatherDesc} \n """
    )

"""Conversion of Current Temperature and Feels-Like Temperature
from F to C respectively."""

# Changing type from str to float for Math Operations
temp_F_float = float(temp_F)
FeelsLikeF_float = float(FeelsLikeF)


def FtoC(F):
    """Convert the units from Fahrenheit to Celsius."""
    C = (5 / 9) * (F - 32)
    # Rounding output to one decimal place
    C_rounded = round(C, 1)
    return C_rounded


# Displaying Temperatures in Celsius from the defined function FtoC
print(f"The Current Temperature in Celsius is {FtoC(temp_F_float)}°C")
print(f"The Feels-Like Temperature in Celsius is {FtoC(FeelsLikeF_float)}°C\n")

# BONUS TASK

# Initializing variable for the current temperature obtained in Celsius
num = FtoC(temp_F_float)

"""Displaying Emojis for Custom Ranges (4 different ranges) of
Current Temperature (in Celsius)"""

if num <= 0:
    print(f"Today's weather in your location: \u2744\uFE0F {num}°C \n")
elif 0.1 <= num <= 15:
    print(f"Today's weather in your location: \u2601\uFE0F {num}°C \n")
elif 15.1 <= num <= 30:
    print(f"Today's weather in your location: \u26C5 {num}°C \n")
elif num > 30:
    print(f"Today's weather in your location:\u2600\uFE0F {num}°C \n")

# BONUS BONUS TASK

"""Since the JSON output has weather forecast data at a 3 hour time step,
retrieving data for 1 time step from now at index 1:"""

three_hours = response["weather"][0]["hourly"][1]

# flt: feels like temperature, at: actual temperature, wd: weather description
next_at_F = three_hours["tempF"]
next_flt_F = three_hours["FeelsLikeF"]
next_at_C = three_hours["tempC"]
next_flt_C = three_hours["FeelsLikeC"]
next_wd = three_hours["weatherDesc"][0]["value"]
print(
    f"""Weather forecast for three hours from now is as follows:
     Current Temperature: {next_at_F}°F = {next_at_C}°C
     Feels like Temperature: {next_flt_F}°F = {next_flt_C}°C
     Weather Description: {next_wd} \n"""
)
