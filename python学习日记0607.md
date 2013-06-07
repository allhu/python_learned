###python学习日记0607

*by cedrichu*

- ####[checkio_task_ATM](http://www.checkio.org/mission/task/atm/)

*task:*
	
#####Teach Sofia how to use an ATM. The ATM on their home island can only dispense $5 bills which means that the machine will not dispense any amount of money that is not divisible by $5. In addition to that, the bank fee for each withdrawal is $1. The robots cannot withdraw any amount above the card’s balance.  



**Input data:** A list of integers: the first one denotes the robot’s account balance, and the second is a list of the monetary amounts that the robot wants to withdraw.

**Output data:** The account balance after all operations (integer).

**Example:**

 	if __name__ == '__main__':
    	assert checkio([120, [10, 20, 30]]) == 57, 'First'
    	
    # With one Insufficient Funds, and then withdraw 10 $
    assert checkio([120, [200, 10]]) == 109, 'Second'
    #with one incorrect amount
    
    assert checkio([120, [3, 10]]) == 109, 'Third'
    assert checkio([120, [200, 119]]) == 120, 'Fourth'
    assert checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56, \
        "It's mixed all base tests"
    print('All Ok')


*code：*

	from math import ceil
	from functools import reduce


	def checkio(data):
    return reduce(lambda a, b, d={}: d.__setitem__(0, (ceil(b * 1.01 + .5))) or a - (not b % 5 and d[0] <= a and d[0] or 0), *reversed(data))

##### 学习摘要
一开始看到这个题目，总觉得其实表达出来挺简单的：

1.取的钱不能大于余额

2.每取一次钱都要扣1块钱，除非你的余额小于5

所以我的思路就是：

判断三种情况：[0:5]、(5:balance)、[balance:无穷大]
发现情况不对，猜测应该是数字要int类型，于是又去搜如何判断字符的type

找到一篇文章：[how to check char is integer in python](http://www.codecho.com/how-to-check-char-is-integer-in-python/)

后来发现还是不OK，整个逻辑也很混乱，此外我的语法还是一塌糊涂，于是看了某位大神的代码，才有上面的答案。

以下是我粗糙的代码，后续熟悉了python，再回过头来解决。


	def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  
    balance, withdrawal = data
    isinstance(withdrawal,int)
    for balance,withdrawal in data:
        x = balance,y = withdrawal
        if 0<y<=5:
            return x-y-y.count()
        if 5< y <X:
            return x-y-y.count()
        if y>=x:
            return x-y.count()
        else:
            return False