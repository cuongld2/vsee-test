from github import Github
import requests
# First create a Github instance:
import os

from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
# using an access token
g = Github(ACCESS_TOKEN)

# # Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

## Total open issues
# for issue in g.get_organization('SeleniumHQ').get_issues(state='open'):
#     print(issue)
# for issue in g.search_issues(query="org:SeleniumHQ",qualifiers="is:open"):
#     print(issue)
# print(f"Total open issues : {g.get_organization('SeleniumHQ').get_issues(state='open').totalCount}")


## All repositories sort by descending updated date
repositories_sorted_list = []
total_open_issues=0
BASE_URL='https://api.github.com'
repo_watcher=0
most_watcher_repositories=[]
for repo in g.get_organization('SeleniumHQ').get_repos(sort="desc"):
    repositories_sorted_list.append(repo.name)
    if repo.watchers > repo_watcher:
        repo_watcher=repo.watchers
        most_watcher_repositories.append(repo.name)

    response = requests.get(f'{BASE_URL}/repos/SeleniumHQ/{repo.name}/issues',params={'state':'open'},headers={'Authorization':f'token {ACCESS_TOKEN}'})
    total_open_issues += len(response.content)

print(repositories_sorted_list)
print(total_open_issues)
print(most_watcher_repositories[-1])
    