
from copy import deepcopy, copy

a = 1
b = a
print(f'b_id = {id(b)} a_id ={id(a)} id_a == id_b: {id(a) == id(b)}')
a = 2
print(f'b_id = {id(b)} a_id ={id(a)} id_a == id_b: {id(a) == id(b)}')

a_list = [1]
b_list = a_list
print(f'b_list_id = {id(b_list)} a_list_id ={id(a_list)} id_a_list == id_b_list: {id(a_list) == id(b_list)}')
b_list = [1]
print(f'b_list_id = {id(b_list)} a_list_id ={id(a_list)} id_a_list == id_b_list: {id(a_list) == id(b_list)}')

a_dic = {1: 2}
b_dic = a_dic
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')
b_dic = {1: 2}
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')

a_dic = {1: [1,2]}
b_dic = a_dic
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')
b_dic = {1: 2}
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')



print(f"-----------------copy --------------------")

a = 1
b = copy(a)
print(f'b_id = {id(b)} a_id ={id(a)} id_a == id_b: {id(a) == id(b)}')
a = 2
print(f'b_id = {id(b)} a_id ={id(a)} id_a == id_b: {id(a) == id(b)}')


print(f"-----------------deepcopy --------------------")

a = 1
b = deepcopy(a)
print(f'b_id = {id(b)} a_id ={id(a)} id_a == id_b: {id(a) == id(b)}')
a = 2
print(f'b_id = {id(b)} a_id ={id(a)} id_a == id_b: {id(a) == id(b)}')

a_list = [1]
b_list = deepcopy(a_list)
print(f'b_list_id = {id(b_list)} a_list_id ={id(a_list)} id_a_list == id_b_list: {id(a_list) == id(b_list)}')
b_list = [1]
print(f'b_list_id = {id(b_list)} a_list_id ={id(a_list)} id_a_list == id_b_list: {id(a_list) == id(b_list)}')

a_dic = {1: 2}
b_dic = deepcopy(a_dic)
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')
b_dic = {1: 2}
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')

a_dic = {1: [1,2]}
b_dic = deepcopy(a_dic)
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')
b_dic = {1: 2}
print(f'b_dic_id = {id(b_dic)} a_dic_id ={id(a_dic)} id_a_dic == id_b_dic: {id(a_dic) == id(b_dic)}')