import random
import time

def sink(arg):
    pass

def wait_long():
    time.sleep(random.uniform(3.0, 5.0))

def wait_short():
    time.sleep(random.uniform(0.5, 1.2))

def wait_micro():
    time.sleep(random.uniform(0.1, 0.4))