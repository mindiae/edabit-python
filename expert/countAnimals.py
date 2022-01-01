# 🦁🐱 Count Animals 🐶🐺
# Mubashir needs your help to find out number of animals hidden in a given string txt.

# You are provided with an array of animals given below:

# animals = ["dog", "cat", "bat", "cock", "cow", "pig",
# "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
# "frog", "hen", "mole", "duck", "goat"]
# Rule: Return the maximum number of animal names. See the below example:

# txt = "goatcode"

# count_animals(txt) ➞ 2
# # First animal = "dog"
# # Remaining string = "atcoe",
# # Second animal = "cat".
# # count = 2 (correct)

# # If you got a "goat" first time
# # remaining string = "code",
# # no animal will be found during next time.
# # count = 1 (wrong)
# Examples
# count_animals("goatcode") ➞ 2
# # "dog", "cat"

# count_animals("cockdogwdufrbir") ➞ 4
# # "cow", "duck", "frog", "bird"

# count_animals("dogdogdogdogdog") ➞ 5
# Notes
# N/A
animals = ["dog", "cat", "bat", "cock", "cow",
  "pig", "fox", "ant", "bird", "lion", "wolf",
  "deer", "bear", "frog", "hen", "mole",
  "duck", "goat"]

def count_animals(txt):
  def countIfAnimalInList(animal, charList):
    list_ = charList.copy()
    for letter in animal:
      if letter in list_:
        list_.remove(letter)
      else:
        return False
    return list_
  def checkIfAnimalInList(animal):
    return isinstance(countIfAnimalInList(animal, listFromTxt), list)
  listFromTxt = list(txt)
  matches = list(filter(checkIfAnimalInList, animals))
  print(matches)
  print(listFromTxt)
  def countLongest(list_, matches, count):
    print(count)
    longestCount = count
    if not matches or not list_:
      return count
    for match in matches:
      if len(list_) < len(match):
        continue
      length1 = 0
      length2 = 0
      animalInList = countIfAnimalInList(match, list_)
      print("animal: ", match)
      print("list_: ", list_)
      print("l: ", animalInList)
      if isinstance(animalInList, list):
        input("animalInList: before countLongest")
        print(f"{animalInList}")
        length1 = countLongest(animalInList,
          matches, count + 1)
        input(f"animalInList: {animalInList} after countLongest")
      else:
        input(f"not animalInList")
        removedFromMatches = matches.copy()
        removedFromMatches.remove(match)
        length2 = countLongest(list_,
          removedFromMatches, count)
      if length1 > length2:
        length = length1
      else:
        length = length2
      if longestCount < length:
        longestCount = length
    return longestCount
  print(countLongest(listFromTxt, matches, 0))
  return countLongest(listFromTxt, matches, 0)


print(count_animals("dogcat") == 2)
print(count_animals("bcaatt") == 2)
print(count_animals("dopig") == 1)
print(count_animals("goatcode") == 2)
print(count_animals("dogdogdogdogdog") == 5)
print(count_animals("cockdogwdufrbir") == 4)
# Mubashir