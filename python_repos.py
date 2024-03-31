import requests #1

# make an API call and store the repsponse
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #2
headers =  {'Accept': 'application/vnd.github.v3+json'} #3
r = requests.get(url, headers=headers) #4
print(f"Status code: {r.status_code}") #5

# Store API response in variable
response_dict = r.json() #6
print(f"Total repositories: {response_dict['total_count']}")

# Explore information abouyt the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the girst repository
repo_dict = repo_dicts[0]

print('\nSelected information about the first repository: ')
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

#Process results
print(response_dict.keys())