# coding=utf-8

import requests
import json

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)

#将API响应存储在一个变量中  打印总共有多少仓库
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Ower:', repo_dict['owner']['login'])
    print('Starts:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])


print("\nKeys: ", len(repo_dict))


# print(response_dict.keys())