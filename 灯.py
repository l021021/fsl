import requests

url = "http://192.168.10.1/api/control"
params = {
    "color": "12357",
    "buzzer": "5",
    "flashe": "11010"
}

response = requests.get(url, params=params)

print(response.text)


# http://192.168.10.1/api/control?clear=1

# http://192.168.10.1/api/control?color=46091&buzzer=5&flashe=01010
