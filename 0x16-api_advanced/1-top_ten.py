#!/usr/bin/python3
"""1. Top Ten"""


def top_ten(subreddit):
    """First 10 hot posts listed for a given subreddit"""
    import requests

    header = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json".
                            format(subreddit), headers=header).json()

    if not response.get('error'):
        top10hot = response.get('data').get('children')[:10]
        titles = []
        if top10hot is not None or top10hot is not []:
            for post in top10hot:
                print(post['data']['title'])
        else:
            print(None)
    else:
        print(None)
