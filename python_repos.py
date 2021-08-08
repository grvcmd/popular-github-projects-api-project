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

# Examine the first repository
first_repository_dictionary = repository_dictionaries[0]
print(f"\nKeys: {len(first_repository_dictionary)}")
for key in sorted(first_repository_dictionary.keys()):
    print(key)

