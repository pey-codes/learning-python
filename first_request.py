import requests

response = requests.get("https://api.github.com/users/pey-codes")
print(response.status_code)
data = response.json()
print(data)
print("pey-codes", "has", data["public_repos"], "public repos")