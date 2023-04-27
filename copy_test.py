import copy

a=[1,2,3]
b=a
c=a.copy()
d=copy.deepcopy(a)
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)

print("ida = ",id(a))
print("idb = ",id(b))
print("idc = ",id(c))
print("idd = ",id(d))

# b.append(4)
d.append(4)

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)

