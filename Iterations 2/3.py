def getMostFreq(str):
    max = 1
    d = {}
    for i in str:
        if i in d:
            count = d[i] + 1
            if count > max:
                max = count
            d[i] = count
        else:
            d[i] = 1
    max_ = []
    for k,v in d.items():
        if v == max:
            max_.append(k)
    return max_

str = input("Enter string: ")
print("Mosst Frequent Characters: ", getMostFreq(str))