#!/usr/bin/python3
"""script hat deletes out-of-date archives, using the function do_clean"""
from fabric.api import *


env.hosts = ['100.25.211.48', '18.234.193.238']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
