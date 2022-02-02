#!/usr/bin/python3
"""0. Gather data from an API"""


if __name__ == "__main__":
    import requests
    import sys

    uid = int(sys.argv[1])
    empl = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(uid))
    name = empl.json().get('name')

    alltasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    alltasks = alltasks.json()
    lsttodos = []
    done_t = 0
    tasks = 0
    for todo in alltasks:
        if todo.get('userId') == uid:
            lsttodos.append(todo)
            if todo.get('completed') is True:
                done_t += 1
            tasks += 1
    print("Employee {} is done with tasks({}/{})".format(name, done_t, tasks))
    for todo in lsttodos:
        if todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
