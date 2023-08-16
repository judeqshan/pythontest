def test(a):
    if a ==1:
        return {"a":1, "b":2}
    else:
        return 1
c = test(1)
print(c)
if 1 == c:
    print("xxxxxxxxxxxx")