import requests
import json

# PushEvent, IssuesEvent, WatchEvent, PullRequestEvent

def get_events(username):
    response = requests.get(f"https://api.github.com/users/{username}/events")
    if response.status_code == 200:
        for event in response.json():
            print(event)
    
get_events("user0246")