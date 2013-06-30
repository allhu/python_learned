###[python学习日记0629]-checkio_space_purchase

*by cedrichu*

- [checkio_task_space_purchase](http://www.checkio.org/mission/task/info/spaceship-purchase/python-27/)

*task:*
	
#####Sofia makes her offer first. She never offers an amount higher than what is offered to her. On the other hand, the old man never offers an amount lower than what is offered to him.


**Input data: **A list of the weights.

**Output data:** A number representing the lowest possible weight difference.

**for exmaple:**

assert checkio([10, 10]) == 0, "1st example"
assert checkio([10]) == 10, "2nd example"
assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
assert checkio([5, 5, 6, 5]) == 1, "4th example"
assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
assert checkio([1, 1, 1, 3]) == 0, "6th example"
t

*code:*

	import random
	def checkio(data):  
    	for i in range(1,k):
       	 half_sum = (reduce（lambda x,y:x+y,data）)/2
        	k = len(data)
    	return min(lambda a:a >= 		half_sum,map(sum(random.sample(data,i))))

but it doesn't work ,so i ask a question on the stackoverflow .

[How to calculate a number representing the lowest possible weight differenc](http://stackoverflow.com/questions/17381252/how-to-calculate-a-number-representing-the-lowest-possible-weight-difference)

some friends help me in the 10minutes! that's cool!

-------------------------------------

Heh... looks you're cheating on http://www.checkio.org/ :)

Anyway, here is the (working) solution is submited there:

	def checkio(stones):
    	def subcheckio(stones, left, rite):
        	if len(stones) == 0:
            	return abs(left - rite)

        	scores = []
        	nstones = stones[1:]
        	scores.append(subcheckio(nstones, left + stones[0], rite))
        	scores.append(subcheckio(nstones, left, rite + stones[0]))

        return min(scores)

    return subcheckio(stones, 0, 0)

Ok, because your question was about fixing your code, here's another version based on what you posted:

	import itertools

	def checkio(data):
    	s = reduce(lambda x,y:x+y,data) # s is the sum, you don't need a loop
   	 half_sum = s / 2

    # instead of random.sample, using itertools to find all possible combinations
    # of all possibles lenghts
    perms = []
    for i in range(len(data) + 1):
        p = itertools.combinations(data, i)
        perms += p

    # min of a list comprehension to find the minimal sum >= half_sum
    m = min([a for a in map(sum, perms) if a >= half_sum])
    # that's the sum of "what's left", members of the list no in the choosen sum
    n = s - m
    # we want the difference between the two
    return abs(n - m)



##### 学习摘要
发现自己在逻辑上其实还有待提高，语法上也还是需要不断去尝试如何提高自己的水平。

感谢这位朋友帮我指出了这个问题，还提供了答案。