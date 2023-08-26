def add_contact(d, name, number):
    if name in d:
        answer = input("duplicate contact do you want to replace it? (y/n)")
        if answer == 'y':
            d[name] = number
        else:
            name2 = input("enter the new name:")
            d[name2] = number

    print("contact added successfully!")


def remove_contact(d, name):
    d.pop(name)
    print("contact removed successfully!")


def find_number(d, name):
    print(d[name])


def find_name(d, number):
    flag = True
    for key in d:
        if d[key] == number:
            flag = False
            print(key)
    if flag:
        print("the contact NotFound...")


def change_name(d, number, new_name):
    flag = True
    for key in d:
        if d[key] == number:
            d.pop(key)
            d[new_name] = number
            flag = False
            break

    if flag:
        print("the contact NotFound...")


dict_ = {"amin": '09123456789', "bardia": '09123344556', 'mahsa': '02177889911', "nika": '02133445511',
         'sina': '0912456879', "sarina": '09013456789', 'kian': '03155155515'}

# add_contact(dict_, "amin", "09123456688")
# remove_contact(dict_, "sina")
change_name(dict_, "02177889911", "kobra")
print(dict_)
