
# dict1 = {'name':'alex','age':18}
# # 18
# # b = dict1.pop('age')
# # print(b)
# a = dict1.popitem()
# # ret = dict1.setdefault('height','188')
# print(a)
# dict2 = dict.fromkeys(['host1','host2','host3'],'test')
# print(dict2)
dict1 = {'name':'alex','age':18}
for k in dict1:
    #print(f'这是格式化的新方法：{k}:{dict1[k]}')
    print('这也是格式化的新方法：{key}:{value}'.format(key=k,value=dict1[k]))