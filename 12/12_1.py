def print_lyrics():
    return 'I\'m a lumberjack , and i\'m okay.\nI sleep all night and work all day'


def repeat_lyrics():
    print_lyrics()
    print()
    print_lyrics()


def greeting(name):
    return f'Hello {name}\nhow are you ?'


def do_twice(f):
    f()
    f()


def twice(f):
    print(f)
    print(f)


x = greeting("ali")
print(x)
