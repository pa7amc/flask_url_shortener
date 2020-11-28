# Importing the required libraries import contextlib
import string
import random


def id_gen(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
