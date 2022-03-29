# Taking input from user for Zip Code, displaying it
zipcode = input("User's US Post Office Zip Code: ")
print(zipcode)

# Importing Libraries
import requests

# Generating URL based on User's Postal Zip Code
url = "http://wttr.in/" + zipcode

# Converting to JSON
params = (('format', 'j1'),)
response = requests.get(url, params=params).json()

# Getting the Current Temperature, Feels-Like Temperature, and Weather Description for user's Zip Code

# The current condition key contains required information hence assigning variable and indexing it
current_condition = response['current_condition'][0]

# Assigning variables and indexing to get Current Temperature, Feels-Like Temperature and Weather Description for user's Zip Code
temp_F = current_condition['temp_F']
FeelsLikeF = current_condition['FeelsLikeF']
weatherDesc = current_condition['weatherDesc'][0]['value']

# Displaying weather conditions with temperatures in Fahrenheit
print(f"The weather conditions in your location are displayed below: \n Current Temperature: {temp_F}°F \n Feels like Temperature: {FeelsLikeF}°F \n Weather Description: {weatherDesc} \n")

# Conversion of Current Temperature and Feels-Like Temperature from F to C respectively.

# Changing type from str to float for Math Operations
temp_F_float = float(temp_F)
FeelsLikeF_float = float(FeelsLikeF)

# Defining a function to convert units from Fahrenheit to Celcius
def FtoC(F):
    C = (5/9) * (F-32)
    # Rounding output to one decimal place
    C_rounded = round(C, 1)
    return C_rounded

# Displaying Temperatures in Celcius from the defined function FtoC
print(f'The Actual Temperature in Celcius is {FtoC(temp_F_float)}°C')
print(f'The Feels-Like Temperature in Celcius is {FtoC(FeelsLikeF_float)}°C \n')

# BONUS TASK

#Initializing variable for the current temperature obtained in Celcius
num = FtoC(temp_F_float)

# Displaying Emojis for Custom Ranges (4 different ranges) of Current Temperature (in Celcius)
if num <= 0:
    print(f"Today's weather in your location: \u2744\uFE0F {num}°C \n")
elif 0.1 <= num <= 15:
    print(f"Today's weather in your location: \u2601\uFE0F {num}°C \n")
elif 15.1 <= num <= 30:
    print(f"Today's weather in your location: \u26C5 {num}°C \n")
elif num > 30:
    print(f"Today's weather in your location:\u2600\uFE0F {num}°C \n")

# BONUS BONUS TASK

# Since the JSON output has weather forecast data at a 3 hour time step, retrieving data for 1 time step from now at index 1:
three_hours = response['weather'][0]['hourly'][1]

#flt = feels like temperature, at = actual temperature, wd = weather description
next_flt = three_hours["FeelsLikeF"]
next_at = three_hours["tempF"]
next_wd = three_hours["weatherDesc"][0]["value"]
print(f'Weather forecast for three hours from now is as follows: \n Feels like Temperature: {next_flt}°F \n Actual Temperature: {next_at}°F \n Weather Description: {next_wd} \n')