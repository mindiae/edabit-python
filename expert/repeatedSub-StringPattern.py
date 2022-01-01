# Repeated Sub-String Pattern
# Create a solution that checks if a given string consists of a sub-string pattern repeated multiple times to return True or False.

# Examples
# repeated("a") ➞ False

# repeated("ababab") ➞ True

# repeated("aba") ➞ False

# repeated("abcabcabcabc") ➞ True

# repeated("aaxxtaaxztaaxxt") ➞ False
# Notes
# Adroit programmers can solve this in one line.
def repeated(s):
  import re
  import math
  for i in range(0, math.floor(len(s)/2)):
    if len(s) % (i + 1) == 0:
      if re.match(r'^('+s[0:i]+r')+$', s):
        return True
  return False

from time import perf_counter
from random import randint
tic = perf_counter()

print(repeated("a") == False)
print(repeated("ababab") == True)
print(repeated("aba") == False)
print(repeated("abcabcabcabc") == True)
print(repeated("aaxxtaaxztaaxxt") == False)

for _ in range(100):
    lst_sub = [randint(97, 122) for _ in range(randint(1, 100))]
    lst_s = lst_sub * randint(2, 100)
    lst_n = lst_s.copy()
    idx_corr = randint(0, len(lst_n) - 1)
    lst_n[idx_corr] = 97 + (lst_n[idx_corr] - 96) % 26
    print(repeated("".join(map(chr, lst_s))) == True)
    print(repeated("".join(map(chr, lst_n))) == False)

print('t_total = {:.6f}'.format(perf_counter() - tic))