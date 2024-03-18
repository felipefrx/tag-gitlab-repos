import requests

private_token = input('Enter the token: ')

tag_name = input('Enter an image tag: ')

file = open('projects-id.txt', 'r')
lines = file.readlines()

for l in lines:
    url = f'https://gitlab.com/api/v4/projects/{l}/repository/tags?tag_name={tag_name}&ref=main'
    r = requests.post(url, headers = {"PRIVATE-TOKEN": private_token})