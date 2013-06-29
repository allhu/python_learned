###[python学习日记0629]-checkio_space_purchase

*by cedrichu*

- [checkio_task_space_purchase](http://www.checkio.org/mission/task/info/spaceship-purchase/python-27/)

*task:*
	
#####Sofia makes her offer first. She never offers an amount higher than what is offered to her. On the other hand, the old man never offers an amount lower than what is offered to him.

**Input data:** Contains four integer numbers: Sofia's initial offer, Sofia's raise to her offer, the initial counteroffer from the old man, and the old man's reduction in his offer;

**Output data:** The amount of money that Sofia will pay for the spaceship.

**Example:**

checkio([150, 50, 1000, 100]) == 450
	
	#Sofia: 200
	#Oldman: 900
	#Sofia: 250
	#Oldman: 800
	#Sofia: 300
	#Oldman: 700
	#Sofia: 350
	#Oldman: 600
	#Sofia: 400
	#Oldman: 500
	#Sofia: 450
	#... old man will be ok with it, because his next proposition will be lower than 450.
 
	# a bit shorter example
	checkio([500, 300, 700, 100]) == 700
	#Sofia will be ok with 700 because her next proposition will be higher


*code：*

	def checkio(data):
    	initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data
    for i in range(1,100):
        if initial_sofi == initial_oldman:
            return initial_sofi
        else:
        	if initial_sofi + i*raise_sofi - initial_oldman + i*reduction_oldman >=0:
        		if initial_sofi + i*raise_sofi > initial_oldman - (i - 1)*reduction_oldman:
        			return initial_oldman - (i - 1)*reduction_oldman
    			else:
    				return initial_sofi + i*raise_sofi

	#These "asserts" using only for self-checking and not necessary for auto-testing
	if __name__ == '__main__':
		assert checkio([150, 50, 1000, 100]) == 450, "1st example"
    	assert checkio([150, 50, 900, 100]) == 400, "2nd example"


	



##### 学习摘要
第二道自己做出来的题目，编程这种事情果然是需要每天都做题，每天都思考。

虽然这个题目逻辑比较简单，但是有很多情况没有考虑到，以后要多关注这些地方的思考方式。