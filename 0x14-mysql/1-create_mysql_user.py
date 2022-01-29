#!/usr/bin/python3
"""Fabric module"""
from fabric.api import local, put, run, env

env.user = 'ubuntu'
env.hosts = ["35.190.145.109", "54.89.149.139"]

s = """SET GLOBAL validate_password_policy=LOW;
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;"""

def create_user():
        run(f"echo \"{s}\" | mysql -uroot -p")
