###python学习日记0605

*by cedrichu*

- ####[checkio_task_sentence-with-extra-spaces](http://www.checkio.org/mission/task/info/sentence-with-extra-spaces/python-3/)

*task:*
	
#####Given string is a sentence, and words should be separated by only one space character. Remove all extra spaces.

**Input data:** A sentence in the string variable.

**Output data:** A sentence without extra spaces.

**Example:**

 	checkio('I  like   python') == "I like python"

*code：*

	#Your optional code here
	#You can import some modules or create additional functions



	def checkio(line):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  

    #replace this for solution
    return " ".join(line.split())

	line = 'I  like  python'
	checkio(line)


