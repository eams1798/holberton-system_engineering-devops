#!/usr/bin/python3
"""2. Recurse it!"""


def hot_recurse(titles, n):
    """Does the recursion"""
    if n < len(titles):
        title = [titles[n].get('data').get('title')]
        return title + hot_recurse(titles, n + 1)
    return [-1]


def recurse(subreddit, hot_list=[], after=None):
    """Function in task #1 but recursive"""
    import requests

    header = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json?after={}".
                            format(subreddit, after), headers=header).json()

    if not response.get('error'):
        after = response.get('data').get('after')
        titles = response.get('data').get('children')
        hot_list.extend(hot_recurse(titles, 0))
        hot_list.remove(-1)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
