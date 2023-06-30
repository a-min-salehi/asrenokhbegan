def histogram (s):
    d = dict ()
    for c in s :
        if c == ' ':
            continue
        
        elif c not in d :
            d[c] = 1
        else :
            d[c] += 1

    return d

def print_hist (h) :

    for k in h :
        print (k , h [k])
        

def sortedPrint_h (h) :

    for i in sorted (h) :
        print (i , h [i])
        
