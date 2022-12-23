import random
import time

_mult = 0.05

def sink(arg):
    pass

def wait_long():
    time.sleep(random.uniform(3.0 * _mult, 5.0 * _mult))

def wait_short():
    time.sleep(random.uniform(0.5 * _mult, 1.2 * _mult))

def wait_micro():
    time.sleep(random.uniform(0.1 * _mult, 0.4 * _mult))