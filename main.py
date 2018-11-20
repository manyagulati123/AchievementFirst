import requests
import json

def getRepos(url, results):
  response = requests.get(url + '&per_page=100')
  repos = json.loads(response.content)
  headers = response.headers
  
  for repo in repos:
    if repo['private'] == False:
      results.append(repo['name'])

  if 'Link' in headers:
    # handle pagination (or the user has more than 100 repositories)
    links = headers['Link'].split(',')
    for link in links:
      if 'next' in link:
        cleanedLink = link.strip().split(';')[0].replace('<', '').replace('>', '')
        getRepos(cleanedLink, results)
        break


def main():
  results = []
  getRepos("https://api.github.com/users/manyagulati123/repos?", results)
  
  for repo in results:
    print repo


main()
