#!/usr/bin/python3
"""0. How many subs?"""

def number_of_subscribers(subreddit):
    """Subscribers of a subreddit"""
    import requests

    header = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get("https://www.reddit.com/r/{}/about.json".
                            format(subreddit), headers=header).json()

    if not response.get('error'):
        subs = response.get('data').get('subscribers')
        if subs is not None:
            return subs
    return 0
