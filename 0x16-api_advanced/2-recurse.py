#!/usr/bin/python3
"""2. Recurse it!"""

def hot_recurse(titles, n):
    """Does the recursion"""
    if (n < len(titles)):
        title = [titles[n].get('data').get('title')]
        return title + hot_recurse(titles, n + 1)
    return [-1]

def recurse(subreddit, hot_list=[]):
    """Function in task #1 but recursive"""
    import requests

    header = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json".
                            format(subreddit), headers=header).json()

    if not response.get('error'):
        titles = response.get('data').get('children')
        hot_list = hot_recurse(titles, 0)
        hot_list.remove(-1)
        return hot_list
    return None