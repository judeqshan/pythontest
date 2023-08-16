test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4} 
  
# 输出原始的字典
print ("字典移除前 : " + str(test_dict)) 
  
# 使用 pop 移除 Zhihu
new_dict = {key:val for key, val in test_dict.items() if key != 'Zhihu'}

# 输出移除后的字典
print ("字典移除后 : " + str(new_dict))


print ("原始 : " + str(test_dict)) 