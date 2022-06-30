import os
from cgitb import html
from mailbox import linesep
from unittest import result

with open('recepies.txt', encoding="utf-8") as f:
    for line in f:
        print(line[1])