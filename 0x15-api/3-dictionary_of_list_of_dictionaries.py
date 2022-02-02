#!/usr/bin/python3
"""3. Dictionary of list of dictionaries"""
if __name__ == "__main__":
    # import pdb
    import requests
    import sys
    import json

    users = requests.get('https://jsonplaceholder.typicode.com/users/')
    users = users.json()

    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = tasks.json()

    dct_users = {}
    todolst = []
    tododct = {}
    uid = 0
    for t in tasks:
        # pdb.set_trace()
        if uid != t.get('userId'):
            dct_users[str(uid)] = todolst
            todolst = []
            uid += 1
        if t.get('userId') == uid:
            tododct["username"] = users[uid - 1].get("username")
            tododct["task"] = t.get("title")
            tododct["completed"] = t.get("completed")
            todolst.append(tododct)
            tododct = {}
    del dct_users['0']
    with open("todo_all_employees.json", "w") as file:
        todojs = json.dumps(dct_users)
        file.write(todojs)
