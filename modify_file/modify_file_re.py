import re
f=open('test3.txt','r')
alllines=f.readlines()
f.close()
f=open('test3.txt','w+')
for eachline in alllines:
    # a=re.sub('hate','love',eachline)
    a=re.sub('\\bhate\\b','love',eachline)
    f.writelines(a)
f.close()