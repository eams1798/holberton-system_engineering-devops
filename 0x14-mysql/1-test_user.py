#!/usr/bin/python3
"""Fabric module"""
from fabric.api import local, put, run, env

env.user = 'ubuntu'
env.hosts = ["35.190.145.109", "54.89.149.139"]

#s = """SHOW GRANTS FOR 'holberton_user'@'localhost'"""

def test_user():
        run("mysql -u holberton_user -p -e \"SHOW GRANTS FOR 'holberton_user'@'localhost'\"")
