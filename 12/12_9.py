def Scope():
    scope='local'
    print(f"scope = {scope}")

scope ='global'

Scope()



def setScope () :
    global scope
    scope='local'

    
print(f"scope = {scope}")

setScope()

print(f"scope = {scope}")

