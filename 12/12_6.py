f = lambda x,y : x**y+y**x

x = int(input('Enter X :'))
y = int(input('Enter y :'))

print('{0}^{1}+{1}^{0} = {2}'.format(x,y,f(x,y)))

print(f'{x}^{y}+{y}^{x} = {f(x,y)}')
#print(f'{y}^{x}+{y}^{x} = {f(x,y)}')
