num = input("enter a number:")
reverse = ""

for i in range(len(num)-1,-1,-1): # '98' , (1, -1 , -1)
    reverse += num[i] # 1 num[1]=> '8' -> reverse = '8' -> num[0] = '9' -> '8' + '9' = '89'

print(int(reverse))
