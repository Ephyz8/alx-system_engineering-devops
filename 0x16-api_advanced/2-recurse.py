#!/usr/bin/python3
"""
Using reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    reslts = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if reslts.status_code == 200:
        after_d = reslts.json().get("data").get("after")
        if after_d is not None:
            after = after_d
            recurse(subreddit, hot_list)
        all_titles = reslts.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
    