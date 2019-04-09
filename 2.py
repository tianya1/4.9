a=10
print (type(a))
b=[1,2,3,4,5]
b[1:3] = [13, 14]
print (b)
c=(1,2,3,4,5)
print (c)
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print (student)
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
for i in range(5):
    print(i)
'''

# ist=[1,2,3,4]
#   it = iter(list)
#   print (next(it))


import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()


for i in range(1, 10):
        for j in range(1, i+1):
            print('{}x{}={}\t'.format(i, j, i*j), end='')
        print()
# 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。
