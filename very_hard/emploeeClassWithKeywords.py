# Employee Class with Keywords
# Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance should have a name and a lastname attribute plus one more attribute for each of the keywords, if any.

# Examples
# john = Employee("John Doe")
# mary = Employee("Mary Major", salary=120000)
# richard = Employee("Richard Roe", salary=110000, height=178)
# giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

# john.name ➞ "John"
# mary.lastname ➞ "Major"
# richard.height ➞ 178
# giancarlo.nationality ➞ "Italian"
# Notes
# First and last names will be separated by whitespace. The test will not include any middle names or initials.
# The value of the keywords can be an int, a str or a list.
class Employee:
	def __init__(self, var1, **kwargs):
	  self.name, self.lastname = var1.split(' ')
	  for k, v, in kwargs.items():
	    setattr(self, k, v)


john = Employee('John Doe')
mary = Employee('Mary Major', salary=120000)
richard = Employee('Richard Roe', salary=110000, height=178)
giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])


print(john.lastname == 'Doe', 'John\'s lastname should be "Doe"')
print(mary.salary == 120000, 'Mary\'s salary should be 120000')
print(richard.height == 178, 'Richard\'s height should be 178')
print(giancarlo.nationality == 'Italian', 'Giancarlo\'s nationality should be "Italian"')
print(peng.subordinates == ['Doe', 'Major', 'Roe', 'Rossi'], 'Peng\'s subordinates should be a list containing 4 strings')