n =  10111123411111117819111111111198711111111111111111
count_l = []
count = 0
mylist = []
mystr = str(n)
for i in mystr:
    mylist.append(i)
for var in mylist:
    if(var == '1'):
        count = count + 1
    else:
        count_l.append(count)
        count = 0
count_l.append(count)
print((count_l))
