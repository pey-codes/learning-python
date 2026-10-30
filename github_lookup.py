import requests

name = input("Enter a GitHub username: ")
try:
    response = requests.get("https://api.github.com/users/" + name)

    if response.status_code == 200:
        data = response.json()
        print("User:", data["login"], "has", data["public_repos"], "public repos and", data["followers"], "followers")
    else:
        print("User not found")
except requests.exceptions.ConnectionError:
    print("Could not connect. Check your internet")