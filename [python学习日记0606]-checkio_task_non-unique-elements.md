###python学习日记0606

*by cedrichu*

- ####[checkio_task_non-unique-elements](http://www.checkio.org/mission/task/info/non-unique-elements/python-3/)

*task:*
	
#####Given a list of integers. You should return a list consisting of only non-unique elements. To do so, you need to remove all unique elements (contained in a given list only once). Don't change the order of a list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].  



**Input data:** A list of integers.

**Output data:** A list of integers.

**Example:**

 	if __name__ == "__main__":
    - assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    - assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    - assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    - assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"

*code：*

	#Your optional code here
	#You can import some modules or create additional functions

	def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  

    #replace this for solution
    return [x for x in data if data.count(x) > 1]

#####学习摘要

刚开始是想要用if条件来做判断：

- 如果X == Y，那么就list.remove（X）。但这样的做法似乎行不通。

后来再github上发现一位开发者已经提供了一个答案，于是照抄下来，顺便学习一下。

	def checkio(data):
        return [x for x in data if data.count(x) > 1]

此处是把所有重复的字符都打印出来，因此[1,1,2,2,3,4,5,5]会输出对应的[1,2,5]