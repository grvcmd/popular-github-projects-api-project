import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an api call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dictionary = r.json()
repository_dictionaries = response_dictionary['items']
repository_names, stars = [], []
for repository_dictionary in repository_dictionaries:
    repository_names.append(repository_dictionary['name'])
    stars.append(repository_dictionary['stargazers_count'])

# Make visualization.
data = [{
    'type': 'bar',
    'x': repository_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repost.html')







