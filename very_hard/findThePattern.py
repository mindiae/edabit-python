# Find the Pattern
# Given a dictionary containing up to six phrases, return a list containing the matching phrases according to the given string (p).
# Ignore any digit that is placed after or before the given string.
# Whether the first letter is capitalized or not, if all letters of the word match the given string (p) == it is valid.
# If it does not match the given string (p) then None.
# Examples
# find_pattern({
#   "Phrase1": "CCOVIDD-19 is no good",
#   "Phrase2": "COVID-18 is no good",
#   "Phrase3": "COVID-17 is no good"
# }, "COVID-19")

# ➞ ["Phrase1 = COVID-19", "Phrase2 = None", "Phrase3 = None"]
# find_pattern({
#   "Phrase1": "Edabit is great",
#   "Phrase2": "Edabit is very great",
#   "Phrase3": "Edabit is really great"
# }, "really")

# ➞ ["Phrase1 = None", "Phrase2 = None", "Phrase3 = really"]
# Notes
# If you are stuck, check the Resources.

def find_pattern(dict_, p):
  import re
  result = [];
  for key in dict_:
    regex = r"(?i)" + p;
    match = re.search(regex, dict_[key]);
    if match:
      result.append(key + " = " + match.group());
    else:
      result.append(key + " = None");
  return result;

print(find_pattern({
        "Phrase1": 'Made in China',
        "Phrase2": 'Made in Brazil',
        "Phrase3": 'Made in America',
        "Phrase4": 'Made in Colombia',
    }, 'Jhonson') == ['Phrase1 = None', 'Phrase2 = None', 'Phrase3 = None', 'Phrase4 = None'])
	
print(find_pattern({
        "Phrase1": 'Edabit is great',
        "Phrase2": 'Edabit is very great',
        "Phrase3": 'Edabit is really great',
    }, 'really') == ['Phrase1 = None', 'Phrase2 = None', 'Phrase3 = really'])
	
print(find_pattern({
        "Phrase1": 'COVID-19 is no good',
        "Phrase2": 'COVID-18 is no good',
        "Phrase3": 'COVID-17 is no good',
    }, 'COVID-19') == ['Phrase1 = COVID-19', 'Phrase2 = None', 'Phrase3 = None'])

print(find_pattern({
        "Phrase1": 'Made12 in China',
        "Phrase2": 'Made in Brazil',
        "Phrase3": '32Made in America',
        "Phrase4": 'Made in Colombia',
    }, 'Made') == ['Phrase1 = Made', 'Phrase2 = Made', 'Phrase3 = Made', 'Phrase4 = Made'])