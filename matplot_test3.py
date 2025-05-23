#--coding:utf-8--
import  matplotlib.pyplot as plt
 
#数据设置
x1 =[0,5000,10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000];
y1=[0, 223, 488, 673, 870, 1027, 1193, 1407, 1609, 1791, 2113, 2388];
 
x2 =[0,5000,10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000];
y2=[0, 214, 445, 627, 800, 956, 1090, 1281, 1489, 1625, 1896, 2151];
 
#设置输出的图片大小
figsize = 11,9
figure, ax = plt.subplots(figsize=figsize)
 
#在同一幅图片上画两条折线
A,=plt.plot(x1,y1,'-r',label='A',linewidth=5.0)
B,=plt.plot(x2,y2,'b-.',label='B',linewidth=5.0)
 
#设置图例并且设置图例的字体及大小
font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 23,
}
legend = plt.legend(handles=[A,B],prop=font1)
 
#设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=23)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
 
#设置横纵坐标的名称以及对应字体格式
font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 30,
}
plt.xlabel('round',font2)
plt.ylabel('value',font2)
 
# plt.xticks([1, 2, 3, 4, 5, 6, 7, 8]) 
plt.xlabel("x轴的名字", fontsize=18)
plt.ylabel("y轴的名字", fontsize=18)  # fontsize=18为名字大小
plt.tick_params('x',labelsize=5)
# plt.xticks(lablesize=1)

 
#将文件保存至文件中并且画出图
# plt.savefig('figure.eps')
plt.show()