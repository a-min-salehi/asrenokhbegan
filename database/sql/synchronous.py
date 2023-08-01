import time

def first():
    print("A")
    time.sleep(2)
    print("B")


def second():
    print("1")
    time.sleep(2)
    print("2")

second()
first()
