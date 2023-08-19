txt = input("enter a string: ")

if any(ch.isdigit() for ch in txt):
    result_txt = ''.join(ch for ch in txt if not ch.isdigit())
else:
    result_txt = txt.lower()

print(result_txt)


        
        
    
