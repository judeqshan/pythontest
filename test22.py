

for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))
    
        


#  if (i == "a" and j != "x") and ((i == "c") and ((j != "x") or (j !="y"))):
#             print(i,j)       