menu = """1.add
2.remove
3.change
4.delete
"""
while True:
    x = int(input(menu))

    if x == 1:
        print("add")

    elif x == 2:
        print("remove")

    elif x == 3:
        print("change")
    elif  x == 4:
        print("delete")
    elif x == 10:
        break
    else:
        print("نامربوط")
