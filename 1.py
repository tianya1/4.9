1.
如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

if age >= 18:
    pass
2.
对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
3.
返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
 x, y = move(100, 100, 60, math.pi / 6)
 print(x, y)
 4.
字符串 可以用转义字符\来标识
Python还允许用r''表示''内部的字符串默认不转义
Python允许用'''...'''的格式表示多行内容
not True
False
None不能理解为0，因为0是有意义的，而None是一个特殊的空值
10 / 3  3.3333333333333335
10 // 3  3
10 % 3   1
5.
Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
ord('A')  65    chr(25991)  '文'
Python对bytes类型的数据用带b前缀的单引号或双引号表示：  x = b'ABC'
6.
'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
7.
list(range(5))
[0, 1, 2, 3, 4]
8.切片
L[0:3] = L[:3]
L[-2:]   记住倒数第一个元素的索引是-1
L[:]  L[::5]
for x, y in [(1, 1), (2, 4), (3, 9)]:
     print(x, y)
使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
