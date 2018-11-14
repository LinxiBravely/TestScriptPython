# coding=utf-8
# 使用列表
# 定义一个列表
list=["a",'b','v','d']
# 打印长度
print(len(list))
# 循环打印
for i in list:
    print i
# 在序列最后插入数据
list.append("5")
for i in list:
    print i

print(list[0])
# 删除序列中的某个元素
del  list[0]
print(list[0])
# 对列表进行排序
list.sort()
print(list)

# 使用元组
zoo = ('wolf', 'elephant', 'penguin')
print 'Number of animals in the zoo is', len(zoo)
new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[2][2]

# 使用字典
ab = { 'Swaroop' : 'swaroopch@byteofpython.info',
'Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com'
}
print "Swaroop's address is %s" % ab['Swaroop']
66
# Adding a key/value pair
ab['Guido'] = 'guido@python.org'
# Deleting a key/value pair
del ab['Spammer']
len(ab)
for name, address in ab.items():
    print (name, address)

# 使用序列
shoplist = ['apple', 'mango', 'carrot', 'banana']
# Indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]
# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]
# Slicing on a string
name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]

# 字符串使用
name = 'Swaroop' # This is a string object
if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'
if 'a' in name:
    print 'Yes, it contains the string "a"'
if name.find('war') != -1:
    print 'Yes, it contains the string "war"'
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)