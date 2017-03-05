import requests

url = "https://na-hackathon-api.arrayent.io:443/v3/devices/33554451"

querystring = {"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJkY2E5MmExMC0wMTFlLTExZTctOTIwNy1iNWMzYjY2M2Y2YTQiLCJlbnZpcm9ubWVudF9pZCI6Ijk0OGUyY2YwLWZkNTItMTFlNi1hZTQ2LTVmYzI0MDQyYTg1MyIsInVzZXJfaWQiOiI5MDAwMTA1Iiwic2NvcGVzIjoie30iLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwiaWF0IjoxNDg4NjYxODU5LCJleHAiOjE0ODk4NzE0NTl9.G72Sa_fojNeBvleaq8k0E9SFC-9RofD4TnqdRg0RLJLbVVbNoEJwTFTCF9EUkW7SwGsJlTlqcB_H9r15nZTXSg"}

payload = "[{\"DeviceAction\": \"led_mode=1\" }, {\"DeviceAction\": \"led_color=0,1,4,4,4\" }]"
headers = {
    'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJkY2E5MmExMC0wMTFlLTExZTctOTIwNy1iNWMzYjY2M2Y2YTQiLCJlbnZpcm9ubWVudF9pZCI6Ijk0OGUyY2YwLWZkNTItMTFlNi1hZTQ2LTVmYzI0MDQyYTg1MyIsInVzZXJfaWQiOiI5MDAwMTA1Iiwic2NvcGVzIjoie30iLCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwiaWF0IjoxNDg4NjYxODU5LCJleHAiOjE0ODk4NzE0NTl9.G72Sa_fojNeBvleaq8k0E9SFC-9RofD4TnqdRg0RLJLbVVbNoEJwTFTCF9EUkW7SwGsJlTlqcB_H9r15nZTXSg",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "fd9b5fef-5b7e-359c-ff1b-0084969a7f22"
    }

response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

print(response.text)