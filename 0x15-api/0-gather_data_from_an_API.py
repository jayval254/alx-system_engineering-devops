#!/usr/bin/python3
"""Python script that returns info about employee TODO list"""
import requests
import sys


if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1]
    first = requests.get('{}/users/{}'.format(api_url, employee_id))
    employee_name = first.json().get('name')
    second = requests.get('{}/todos?userId={}'.format(api_url, employee_id))
    responses = second.json()
    done_tasks = [t for t in responses if t.get('completed')]
    print('Employee {} is done with tasks({}/{}):'.
          format(employee_name, len(done_tasks), len(responses)))
    for t in done_tasks:
        print('\t {}'.format(t.get('title')))
