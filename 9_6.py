for i in range(2,51): #2 3
        is_prime = True
        for j in range(2,int(i**0.5)+1): # (2,3 ,4)
            if i%j == 0 :
                is_prime = False
                break
        if is_prime : #True #False
            print(i,end=" ")
