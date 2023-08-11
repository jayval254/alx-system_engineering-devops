#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10 hot posts"""
import json
import requests
import sys


def top_ten(subreddit):
    """ return hot posts """
    subreddit_exists = requests.get(
        "https://reddit.com/r/{}".format(subreddit),
        headers={'User-agent': 'test'})
    if subreddit_exists.status_code == 200:
        hot_posts_req = requests.get(
            "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit),
            headers={'User-agent': 'test'})
        for post in list(hot_posts_req.json().get("data").get(
                "children")):
            print(post.get("data").get("title"))
    else:
        print(None)
