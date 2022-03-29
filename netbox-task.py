# taking input from the user for their Zip Code and displaying it
zipcode = input("User's US Post Office Zip Code: ")
print(zipcode)

# importing libraries
import requests

# generating url based on user's zip code
url = "http://wttr.in/" + zipcode

# getting JSON weather report
params = (('format', 'j1'),)
response = requests.get(url, params=params).json()
# printing json output
# print(response.json())

# getting the current temp, feels like temp, and weather description for user's zip code

# generating different params for all above mentioned
params1 = (('format', '"Current Temperature: %t"'),)
r_t = requests.get(url, params=params1).json()
params2 = (('format', '"Feels like Temperature: %f"'),)
r_f = requests.get(url, params=params2).json()
params3 = (('format', '"Weather Description: %C"'),)
r_C = requests.get(url, params=params3).json()

print('The weather conditions in your location are displayed below:',"\n",r_t,"\n",r_f,"\n",r_C)


# Conversion of current temperature from F to C.

# retrieving current temperature 
t_param = (('format', '"%t"'),)
current_temp = requests.get(url, params=t_param).json()
# slicing to get sign and digits of temperature, converting string to float
F_current = float(current_temp[0:3])

# converting fahrenheit to celcius and rounding it to one decimal
C_current = round(((5/9) * (F_current-32)), 1)
print(f'The Actual Temperature in Celcius is {C_current}°C')


# Conversion of feels-like temperature now from F to C.

# retrieving feels like temp now
feel_t_param = (('format', '"%f"'),)
feels_like_temp = requests.get(url, params=feel_t_param).json()
# slicing to get sign and digits of temperature, converting string to float
F_feels_like = float(feels_like_temp[0:3])

# converting fahrenheit to celcius and rounding it to one decimal
C_feels_like = round(((5/9) * (F_feels_like-32)),1)
print(f'The Feels-Like Temperature in Celcius is {C_feels_like}°C')

# BONUS TASK

# emojis for ranges of temp 
num = C_current
# custom ranges (4 different ranges)
if num <= 0:
    print(f"Today's weather in your location: \u2744\uFE0F, {num}°C")
elif 0.1 <= num <= 15:
    print(f"Today's weather in your location: \u2601\uFE0F, {num}°C")
elif 15.1 <= num <= 30:
    print(f"Today's weather in your location: \u26C5, {num}°C")
elif num > 30:
    print(f"Today's weather in your location:\u2600\uFE0F, {num}°C")

# BONUS BONUS TASK

print(f'Weather forecast for three hours from now is as follows:')

# we know that the json output has weather forecast data at a 3 hour time step
# retrieving data for 1 time step from now (at index 1)
three_hours = response['weather'][0]['hourly'][1]

#flt = feels like temperature, ct = current temperature, wd = weather description
next_flt = three_hours["FeelsLikeF"]
next_ct = three_hours["tempF"]
next_wd = three_hours["weatherDesc"][0]["value"]
print(f'\n Feels like Temperature: {next_flt}°F \n Current Temperature: {next_ct}°F \n Weather Description: {next_wd}')