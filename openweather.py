import requests


class files:
    def __init__(self, city, country):
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=d0e33dc76f8bfc1ef08868bc7c2568b1&units=metric"
        self.city = city
        self.country = country
        self.internetcheck = False
        try:
            self.res = requests.get(self.url)
            self.data = self.res.json()
        except requests.exceptions.ConnectionError:
            self.internetcheck = True
            print('Error connecting to Openweather.org, check your internet connection.')


class info:
    def __init__(self):
        self.city = input('What city do you want to search for? ')
        self.country = input("What's your country code? Ex: US : ")
        self.check = False
        if not files(self.city, self.country).internetcheck:
            data = files(self.city, self.country).data
            try:
                self.temp = data['main']['temp']
                self.tempmin = data['main']['temp_min']
                self.tempmax = data['main']['temp_max']
                self.forecast = data['weather'][0]['main']
                self.forecastprecision = data['weather'][0]['description']
                self.humidity = data['main']['humidity']
                self.wind = data['wind']['speed']
                self.feelslike = data['main']['feels_like']
            except KeyError:
                self.check = True
                print('Error finding weather for that location. Check for typos.')

    def __str__(self):
        if not self.check:
            try:
                errortrigger = {self.temp}
                print("FORECAST:\n")
                print(f"City: {self.city}")
                print(f"Temperature: {self.temp}°c, Feels like {self.feelslike}°c, Minimum and Maximum : {self.tempmin}°c < {self.tempmax}°c")
                print(f"Weather : {self.forecast} or more precisely {self.forecastprecision}")
                print(f"Wind : {self.wind}KM/hr")
            except AttributeError:
                quit()
info().__str__()
