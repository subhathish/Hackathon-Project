import requests

api_key = "AAAAPPPPIIII_____KKKKEEEEYYYY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]
    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +

        "\n Temperature in Degree Celsius: " +str(current_temperature - 272.15)+
          "\n description = " +
                    str(weather_description))
else:
    print(" City Not Found ")