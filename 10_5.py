txt = input("enter a string: ")

any_number = False

for ch in txt:
    if ch.isdigit():
        any_number = True
        txt = txt.replace(ch,'')

if not any_number:
    txt = txt.lower()


print(txt)
        
        
    
