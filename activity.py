import requests
import json

# PushEvent, IssuesEvent, WatchEvent, CreateEvent

def get_events(username):
    response = requests.get(f"https://api.github.com/users/{username}/events")
    if response.status_code == 200:
        for event in response.json():
            if event['type'] == 'PushEvent':
                print(f"{event['actor']['login']} push to {event['repo']['name']} (branch: {event['payload']['ref'].split('/')[-1]})") 
            elif event['type'] == 'IssuesEvent':
                print(f"{event['actor']['login']} {event['payload']['action']} issue") 
            elif event['type'] == 'WatchEvent':
                print(f"{event['actor']['login']} starred {event['repo']['name']}")
            elif event['type'] == 'CreateEvent':
                print(f"{event['actor']['login']} create {event['payload']['ref_type']} at {event['repo']['name']}")
            else:
                print(event)
    
get_events("user0246")