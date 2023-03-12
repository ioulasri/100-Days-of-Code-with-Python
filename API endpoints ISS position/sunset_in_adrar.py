import requests


def add_hour(h):
    a = int(h[0]) + 1
    return str(a) + ":" + h[1] + ":" + h[2]


param = {
    "lat": 30.385500,
    "lng": -9.503068,
    "formatted": 1,
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=param)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split(":")
sunset = data["results"]["sunset"].split(":")
print("sunrise :", add_hour(sunrise))
print("sunset :", add_hour(sunset))

