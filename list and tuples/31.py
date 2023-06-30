def invertDict(d):
    inverse = {}

    for key in d :
        val = d[key]
        if val not in inverse :
            inverse[val] = [key]
        else :
            inverse[val].append(key)

    return inverse
