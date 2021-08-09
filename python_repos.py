import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total respositories: {response_dict['total_count']}")

# Explore information about the repositories.
repository_dictionaries = response_dict['items']
print(f'Repositories returned: {len(repository_dictionaries)}')

print("\nSelected information about each repository:")
for repository_dictionary in repository_dictionaries:
    print(f"\nName: {repository_dictionary['name']}")
    print(f"Owner: {repository_dictionary['owner']['login']}")
    print(f"Stars: {repository_dictionary['stargazers_count']}")
    print(f"Repository: {repository_dictionary['html_url']}")
    print(f"Description: {repository_dictionary['description']}")

