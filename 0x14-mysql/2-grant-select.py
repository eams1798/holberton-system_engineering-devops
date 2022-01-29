#!/usr/bin/python3
"""Fabric module"""
from fabric.api import local, put, run, env

env.user = 'ubuntu'
env.hosts = ["35.190.145.109", "54.89.149.139"]

s = """GRANT SELECT ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;"""

def grant_select():
        run(f"echo \"{s}\" | mysql -uroot -p")
