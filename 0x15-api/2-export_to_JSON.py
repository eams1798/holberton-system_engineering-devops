#!/usr/bin/python3
"""2. Export to JSON"""
if __name__ == "__main__":
    import requests
    import sys

    uid = int(sys.argv[1])
    empl = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(uid))
    name = empl.json().get('username')

    alltasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    alltasks = alltasks.json()
    todo = []
    for t in alltasks:
        if t.get('userId') == uid:
            todo.append(t)
    strdict = ""
    for n in range(len(todo)):
        task = "\"task\": \"{}\"".format(todo[n].get('title'))
        completed = "\"completed\": {}".format(str(todo[n].get('completed'))
                                               .lower())
        username = "\"username\": \"{}\"".format(name)
        strdict += "{{{0}, {1}, {2}}}".format(task, completed, username)
        if n != len(todo) - 1:
            strdict += ", "
    filetext = "{{\"{0}\": [{1}]}}".format(uid, strdict)
    with open("{}.json".format(uid), "w") as file:
        file.write(filetext)
