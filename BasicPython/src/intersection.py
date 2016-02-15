def intersect(seq1, seq2):
    res = []                     # start empty
    for x in seq1:               # scan seq1
        if x in seq2:            # common item?
            res.append(x)        # add to end
    return res

s1 = [1, 2, 3]
s2 = [1, 4]
x = intersect(s1,s2)    # mixed types
print("Intersection is X -> ", x)                                   # saved result object
