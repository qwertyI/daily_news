import requests
import json
import MySQLdb


def a(func):
    def wrapper(d):
        print func.__name__
        func(d)
        print 'a'
    return wrapper


def c(func):
    def wrapper(d):
        print func.__name__
        func(d)
        print 'c'
    return wrapper


@c
@a
def b(d):
    # type: () -> object
    print d

b('ning')
