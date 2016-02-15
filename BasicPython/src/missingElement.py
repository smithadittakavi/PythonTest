L = [1,2,3,9]
prev = L[0]
for this in L[1:]:
    if this > prev+1:
        for item in range(prev+1, this):    # this handles gaps of 1 or more
            print(item)
    prev = this



