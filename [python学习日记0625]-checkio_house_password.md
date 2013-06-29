###python学习日记0625

*by cedrichu*

- ####[checkio_task_house_password]http://www.checkio.org/mission/task/info/house-password)

*task:*
	
#####Help Nikola develop a password security check module for Sofia. The password will be considered strong enough if its length is greater than or equal 10 symbols, it has at least one number, one uppercase letter and one lowercase letter in it.

**Input data:** A string that is a password.

**Output data:** The output will be true if the password is safe.

**Example:**

checkio('A1213pokl')==False

checkio('bAse730onE')==True

checkio('asasasasasasasaas')==False

checkio('QWERTYqwerty')==False

checkio('123456123456')==False

checkio('QwErTy911poqqqq')==True


*code：*

	#随机密码生成
	from random import Random
	import string
	def  checkio(data):
		seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		key = []
		for i in range(10):
			key.append(Random.choice(seed))
		data = ''.join(key)
		print data
	
	#the answer of house password
	#判断密码是否符合强密码的标注
	from functools import partial
	from operator import lt


	def checkio(data):
    	'Return True if password strong and False if not'
    	checks = [str.isdigit, str.islower, str.isupper]
    	return len(data) >= 10 and all(map(lambda fn: any(map(fn, data)), checks))

##### 学习摘要
一开始理解错误以为是需要一个生成随机密码的任务，于是又了第一部分的代码。实际上这个任务是要提供一个条件，判断密码是否符合要求。

不过也好，第一部分的代码让我学习了如何用random和string，包括append这样的基础操作

第二部分还在学习，正好在前几个任务都看到了functools这个库的应用，今天回去学习了解一下这个库的命令。