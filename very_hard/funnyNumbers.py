#Funny Numbers
#Mubashir was playing with some numbers. He observed some funny numbers.

#Funny Numbers
#89 --> 8¹ + 9² = 89 * 1

#695 --> 6² + 9³ + 5⁴ = 1390 = 695 * 2

#46288 --> 4³ + 6⁴ + 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#Create a function which takes a number n and a positive integer p and returns a positive integer k, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

#In other words, is there an integer k such as:

#(a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ... ) = n * k
# A given number = n
# A given positive integer = p
# Digits of the given number = a, b, c, d ...
# A positive integer = k
#Your function should return None if k is not found.

#Examples
#funny_numbers(89, 1) ➞ 1
# since 8¹ + 9² = 89 = 89 * 1

#funny_numbers(92, 1) ➞ None
# since there is no k such as 9¹ + 2² equals 92 * k

#funny_numbers(695, 2) ➞ 2
# 6² + 9³ + 5⁴= 1390 = 695 * 2
#Notes
#Given number and power will always >=1

def funny_numbers(n, p):
	string = str(n)
	sumOfPowers = 0
	for i in range(0, len(string)):
	  sumOfPowers += int(string[i]) ** (p + i)
	result = sumOfPowers / n
	return int(result) if result == int(result) else None

print(funny_numbers(89, 1) == 1)
print(funny_numbers(92, 1) == None)
print(funny_numbers(46288, 3) == 51)
print(funny_numbers(114, 3) == 9)
print(funny_numbers(46288, 5) == None)
print(funny_numbers(135, 1) == 1)
print(funny_numbers(175, 1) == 1)
print(funny_numbers(518, 1) == 1)
print(funny_numbers(598, 1) == 1)
print(funny_numbers(1306, 1) == 1)
print(funny_numbers(2427, 1) == 1)
print(funny_numbers(2646798, 1) == 1)
print(funny_numbers(3456789, 1) == None)
print(funny_numbers(3456789, 5) == None)
print(funny_numbers(198, 1) == 3)
print(funny_numbers(249, 1) == 3)
print(funny_numbers(1377, 1) == 2)
print(funny_numbers(1676, 1) == 1)
print(funny_numbers(695, 2) == 2)
print(funny_numbers(1878, 2) == 19)
print(funny_numbers(7388, 2) == 5)
print(funny_numbers(47016, 2) == 1)
print(funny_numbers(542186, 2) == 1)
print(funny_numbers(261, 3) == 5)
print(funny_numbers(1385, 3) == 35)
print(funny_numbers(2697, 3) == 66)
print(funny_numbers(6376, 3) == 10)
print(funny_numbers(6714, 3) == 1)
print(funny_numbers(63760, 3) == 1)
print(funny_numbers(63761, 3) == 1)
print(funny_numbers(132921, 3) == 4)
print(funny_numbers(10383, 6) == 12933)
#Mubashir