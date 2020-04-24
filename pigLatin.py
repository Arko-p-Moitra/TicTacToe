def myfunc(str='ABC'):
    newstr=' '
    item=0
    while item < len(str):
        if item==0 :
           newstr = newstr + str[item].lower()
        elif item!=0 and item %2 ==0 :
            newstr = newstr + str[item].upper()
        item=+1
    print( newstr)

