###python学习日记0626

*by cedrichu*

- [checkio_task_speech_module](http://www.checkio.org/mission/task/info/speechmodule/python-27/)

*task:*
	
#####Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and faster by writing his speech module. All the words in the string must be separated by exactly one space character.

**Input:** Integer number from 0 to 999.

**Output:** A string representation of this number.

**Example:**
assert checkio(4) == 'four', "1st example"
    
assert checkio(133) == 'one hundred thirty three', "2nd example"
    
assert checkio(12) == 'twelve', "3rd example"

assert checkio(101) == 'one hundred one', "4th example"

assert checkio(212) == 'two hundred twelve', "5th example"

assert checkio(40) == 'forty', "6th example"


*code：*

	def checkio(number):
    isinstance(number, int)

    X = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen","seventeen","eighteen","nineteen"]
    Y= ["twenty", "thirty", "forty", "fifty", "sixty", "seventy","eighty", "ninety"]

    if 0 <= number < 20:
        return X[number]
    if number == 20:
        return 'twenty'
    if 100 > number > 20:
        if number % 10 != 0:
            return Y[number/10 - 2]+' ' + X[number % 10]
        else:
            return Y[number/10 - 2]
    if number == 100:
        return 'one hundred'
    if 120 >number > 100:
        return X[number/100]+' '+'hundred'+' '+ X[number % 100]

    if number == 120:
        return 'one hundred twenty'
    if number > 120:
        if number % 100 /10 >2:
            return X[number/100] + ' ' + 'hundred' + ' ' + Y[(number % 100) /10 - 2]+ ' ' + X[(number%100) % 10]
        if number % 100 / 10 == 0：
        	return X[number/100] + ' ' + 'hundred'   
        else:
            return X[number/100] + ' ' + 'hundred' + ' '  + X[number%100]
    checkio(number)

	#重构逻辑
	FIRST_TEN = ["zero", "one", "two", "three", "four", 	"five", "six", "seven", "eight", "nine"] 
	SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", 	"fourteen", "fifteen", "sixteen", "seventeen", 	"eighteen", "nineteen"]
	OTHER_TENS = ["twenty", "thirty", "forty", "fifty", 	"sixty", "seventy", "eighty", "ninety"]
	HUNDRED = "hundred"

	def checkio(number):
    	if number < 10:
        	return FIRST_TEN[number]
    	elif number >= 10 and number < 20:
        	return SECOND_TEN[number - 10]
    	elif number >= 20 and number < 100:
        	if number % 10 != 0:
            return OTHER_TENS[number / 10 - 2] + " " + checkio(number % 10)
        	else:
            return OTHER_TENS[number / 10 - 2]
		else:
       		if number % 100 == 0:
            	return FIRST_TEN[number / 100] + " " + HUNDRED
        	else:
            	return FIRST_TEN[number / 100] + " " + HUNDRED + " " + checkio(number % 100)



	



##### 学习摘要
逻辑是关键，需要细心地去判断个位是0，十位是2的情况，还要考虑数字不能大于10000，还需要判断number的有效性。

这个应该是我第一个独立完成的一个题目，还是比较有成就感的。希望可以保持这股学习的热情，继续下去！