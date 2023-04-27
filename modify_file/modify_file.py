fp = open('test2.txt','w+')  #打开你要写得文件test2.txt
lines = open('D:\\workspace\\pythontest\\pythontest-main\\modify_file\\test1.txt').readlines()  #打开文件，读入每一行
for s in lines:
    print(s)
    print(s.replace('love','hate').replace('yes','no'))
    fp.write( s.replace('love','hate').replace('yes','no'))    # replace是替换，write是写入
fp.close()  # 关闭文件

