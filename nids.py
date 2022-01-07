import requests

# resp = requests.get(url="http://api.open-notify.org/iss-now.json" )
resp = requests.get(url="http://api.sunrise-sunset.org/json", )
print('Response=', resp)

resp.raise_for_status       # throws exception if something goes wrong
# print(resp.status_code)                  # gives status 404,200,500
print(resp.json())
# print(resp.json()['iss_position']['longitude'])
