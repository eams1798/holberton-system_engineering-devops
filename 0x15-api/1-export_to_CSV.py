#!/usr/bin/python3
"""1. Export to CSV"""
if __name__ == "__main__":
    import requests
    import sys

    uid = int(sys.argv[1])
    empl = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(uid))
    name = empl.json().get('username')

    alltasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    alltasks = alltasks.json()
    lsttodos = []
    for todo in alltasks:
        if todo.get('userId') == uid:
            lsttodos.append(todo)
    with open("{}.csv".format(uid), "w") as file:
        for todo in lsttodos:
            completed = todo.get("completed")
            task = todo.get("title")
            file.write("\"{}\",\"{}\",\"{}\",\"{}\"\n"
                       .format(uid, name, completed, task))
