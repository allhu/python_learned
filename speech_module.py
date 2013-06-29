def checkio(number):
    isinstance(number, int)

    X = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
    Y= ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]

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

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
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


