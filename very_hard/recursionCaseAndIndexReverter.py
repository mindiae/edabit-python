# Recursion: Case and Index Inverter
# Write a recursive function that takes a string input and returns the string in a reversed case and order.

# Examples
# invert("dLROW YM sI HsEt") ➞ "TeSh iS my worlD"

# invert("ytInIUgAsnOc") ➞ "CoNSaGuiNiTY"

# invert("step on NO PETS") ➞ "step on NO PETS"

# invert("XeLPMoC YTiReTXeD") ➞ "dExtErIty cOmplEx"
# Notes
# No empty strings and will neither contain special characters nor punctuation.
# You are expected to solve this challenge using a recursive approach.
# You can check on the Resources tab for more details about recursion.
# An iterative version of this challenge can be found via this link.
def invert(s):
  import math
  # your recursive solution here
  s = s.swapcase()
  index = math.floor((len(s)-1)/2)
  if len(s)%2 == 0:
    middle = ""
  else:
    middle = s[index]
    index -= 1
  def buildFromMiddle(string, index):
    string = s[-(index +1)] + string
    string += s[index]
    if index == 0:
      return string
    return buildFromMiddle(string, index - 1)
  return buildFromMiddle(middle, index)

from re import findall, MULTILINE
from inspect import getsource

def check_recursive(fn):
  try:
    src, n = getsource(fn), fn.__name__
    if n == '<lambda>': n = src.split('=')[0].strip()
    return len(findall(n, src, flags=MULTILINE)) > 1
  except OSError: return True

print('Recursion is required!' if check_recursive(invert) == False else "")

str_vector, res_vector = [
  "dLROW YM sI HsEt", "This string is CASE and INDEX reversed", "ReVeRsIbLe", "rAmIfIcAtIoN", "IntellectualS",
  "DESREVER xedni DNA esac SI GNIRTS SIHt", "ElBiSrEvEr", "nOiTaCiFiMaR", "sLAUTCELLETNi",
  "CoNSaGuiNiTY", "step on NO PETS", "dExtErIty cOmplEx"
], [
  "TeSh iS my worlD", "DESREVER xedni DNA esac SI GNIRTS SIHt", "ElBiSrEvEr", "nOiTaCiFiMaR", "sLAUTCELLETNi",
  "This string is CASE and INDEX reversed", "ReVeRsIbLe", "rAmIfIcAtIoN", "IntellectualS",
  "ytInIUgAsnOc", "step on NO PETS", "XeLPMoC YTiReTXeD"
]
for i, n in enumerate(str_vector): print(invert(n) == res_vector[i])