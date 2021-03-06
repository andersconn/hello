#!/usr/bin/env python3

import skilstak.colors as c
import time

def print_plain(message):
    """Clears screen and prints 'Hello World."""
    print(c.clear + message + c.reset)

def print_color(message):
    """Prints hello in color"""
    print(c.clear)
    while True:
        print(c.rc() + message + c.reset, end =" ")        

def print_multi(message):        
    """prints 'hello world' in fancy random colors"""
    while True:
        print(c.clear + c.multi(message))
        time.sleep(0.5)

def parse_args():
    from sys import argv as a
    who = "world"
    option = ""
    message = ""
    if len(a) > 2:
        option = a[1]
        who = a[2]
    elif len(a) == 2:
        if a[1].startswith("-"):
            option = a[1]
        else:
            who = a[1]
    return who, option



