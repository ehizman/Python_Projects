import requests

username = "ehizman"

github_url = f"https://api.github.com/users/{username}/followers"

response = requests.get(github_url)

for details in response:
    print(details)
