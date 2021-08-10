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
repository_links, stars, labels = [], [], []
for repository_dictionary in repository_dictionaries:
    repository_name = repository_dictionary['name']
    repository_url = repository_dictionary['html_url']
    repository_link = f"<a href='{repository_url}'>{repository_name}</a>"
    repository_links.append(repository_link)

    stars.append(repository_dictionary['stargazers_count'])

    owner = repository_dictionary['owner']['login']
    description = repository_dictionary['description']
    label = f"Owner: {owner}<br>About: {description}"
    labels.append(label)

# Make visualization.
data = [{
    'type': 'bar',
    'x': repository_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24, 'color': 'green'},
        'tickfont': {'size': 14, 'color': 'green'},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24, 'color': 'rebeccapurple'},
        'tickfont': {'size': 14, 'color': 'rebeccapurple'},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')







