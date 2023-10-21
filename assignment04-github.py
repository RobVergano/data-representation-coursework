# Assignment 04:
# Write a program in python that will read a file from a repository.
# The program should then replace all the instances of the text "Andrew" with your name.
# The program should then commit those changes and push the file back to the repository.

# Module to interact with GitHub API:
from github import Github
# Module to retreive the API Key:
from gitkey import config as cfg
# Module for HTTP requests:
import requests

# Retreive the API key from config to create a GitHub object "g" which allows access to the private repository.
apikey = cfg["configkey"]
g = Github(apikey)

# Variables to be replaced:
old_string = "Andrew"
new_string = "Roberto"

# Target repository and file to update:
target_repo = "RobVergano/privateone"
target_file = "testfile"

# get_file function: it retrieves the content and path from the target file.
def get_file(target_repo, target_file):
    repo = g.get_repo(target_repo)
    file_info = repo.get_contents(target_file)
    url_file = file_info.download_url
    response = requests.get(url_file)
    content_file = response.text
    return content_file, file_info

# replace_string function: it replaces a target string for another from the downloaded file. Ref: https://www.w3schools.com/python/ref_string_replace.asp
def replace_string(original_content):
    new_content = original_content.replace(old_string, new_string)
    return new_content
 
# update_github function: takes the file with the new string and updates the file on GitHub. It retrieves the GitHub API response.
def update_github(repo, file_info, new_content):
    gitHubResponse = repo.update_file(file_info.path, "updated by Rob", new_content, file_info.sha)
    return gitHubResponse

# Call the functions. Retrieve the content and path from target file using get_file function:
original_content, file_info = get_file(target_repo, target_file)

# Replace the target string for the new one using replace_string function:
new_content = replace_string(original_content)

# Get the target reporsitory:
repo = g.get_repo(target_repo)

# Update the file on GitHub using update_github function and prints the GitHub API response:
git_response = update_github(repo, file_info, new_content)
print(git_response)


