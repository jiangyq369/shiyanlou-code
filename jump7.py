i = 1
while i < 101:
    if i%10 == 7 or i%7 == 0 or i//10 == 7:
        pass
    else:
        print(i,end = ' ')
    i += 1
