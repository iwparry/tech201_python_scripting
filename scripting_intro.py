# Scripting
import math
# Shorter pieces of code that allow us to do things we would otherwise have to do manually
# Unlike programs, scripts are one file and do not need to be compiled
# API's tend to use scripts
# Scripts use less or no abstraction and are not as flexible as programs but they are much easier to read and write

# Scripts are almost always written in 'high level' languages (easy to read) - Python, Bash, Ruby, Node.js

# Why Python

# Open Sources
# Many Libraries
# Easy to understand
# Large community
# Language interoperability (can talk to other languages, OS's and software)

# Why is Scripting Important for DevOps Engineers?

# Automation -> Of mundane tasks

# 7 core modules in Python
# Sys
# OS
# Subprocesses
# Math
# Random
# DateTime
# Json

# Sys Module Scripts
import sys

print(sys.version)

# OS Module Scripts
import os

print(os.getcwd())
# os.chdir("C:\Users\iwpar\PycharmProjects") # changes directory

# os.mkdir("path") # makes directory

# Subprocesses Module Script
# This module can be used to create and interact with subprocesses being managed by our Python Interpretor

import subprocess

subprocess.run(["python", "hello_world.py"])

# Math Module Scripts
import math

pi = math.pi
pi_string = str(pi)
print("The value of pi is", pi_string)

# Random Module Scripts
import random

randnum = random.randrange(1, 10)
print(randnum)

# DateTime Module Scripts
import datetime

what_is_the_date = datetime.datetime.now()
print(what_is_the_date)

# JSON Module Scripts
import json

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}
y = json.dumps(x)
print(y)