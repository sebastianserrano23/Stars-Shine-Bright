import requests

# make an API call and store the repsponse
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers =  {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in variable
response_dict = r.json()

#Process results
print(response_dict.keys())