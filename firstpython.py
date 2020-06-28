import math
import os
import sys
from os import rename

import requests

print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# name = input("What is your name..?")
# print("Good Morning says Junior", name)

print("HOLA1")
print("HOLA")
print(greet("World"))
print(greet("Roberto"))


r = requests.get("https://www.python.org")
r.status_code


print(r.status_code)
