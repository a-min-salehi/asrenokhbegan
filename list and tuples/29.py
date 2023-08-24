def histogram (s):
    d = dict ()
    for char in s :
        if char == ' ':
            continue
        
        elif char not in d :
            d[char] = 1
        else :
            d[char] += 1

    return d

def print_hist (h) :

    for k in h :
        print (k , h [k])
        

def sortedPrint_h (h) :

    for i in sorted (h) :
        print (i , h [i])


def value_sort_h (my_dict):
    dict_item = my_dict.items() # -> {'s': 1,"a": 2 , ... } >>> [('s',1),("a",2), ...]
    sorted_dict = dict (sorted(dict_item , key=lambda x: x[1], reverse= True))
    for i in sorted_dict :
        print (i , sorted_dict[i])
        
