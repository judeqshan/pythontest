tour = []
height = []

hei = 100
time = 10
for i in range(1, time+1):
    if i == 1:
        tour.append(hei)
    else:
        tour.append(hei*2)
    hei /= 2
    height.append(hei)

print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))