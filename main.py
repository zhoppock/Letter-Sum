# Hoppock, Zachary
# letterSum.py
# Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.
# Version # 1
import string
import time

def min_and_sec(start, end):
  minutes = (end - start) // 60
  seconds = (end - start) % 60
  print("Processing time:", minutes, "minutes and %.2f seconds." % seconds)
  
def listToDict(lst):
    op = {lst[i]: i + 1 for i in range(len(lst))}
    return op

def lettersum(word):
  numAlph = listToDict(string.ascii_lowercase)
  sum = 0
  for i in range(len(word)):
    sum += numAlph[word[i]]
  return sum

print("The letter sum of '' is", lettersum(""))
print("The letter sum of 'a' is", lettersum("a"))
print("The letter sum of 'z' is", lettersum("z"))
print("The letter sum of 'cab' is", lettersum("cab"))
print("The letter sum of 'excellent' is", lettersum("excellent"))
print("The letter sum of 'microspectrophotometries' is", lettersum("microspectrophotometries"))

print("\nOptional bonus challenges")

print("\n 1. microspectrophotometries is the only word with a letter sum of 317. Find the only word with a letter sum of 319.")
words_list = [ line.strip() for line in open("words.txt") ]
start = time.time()
for i in range(len(words_list)):
  if lettersum(words_list[i]) == 319:
    print(" - The only word with the letter sum of 319 is", words_list[i])
    break
end = time.time()
min_and_sec(start, end)

print("\n 2. How many words have an odd letter sum?")
count = 0
start = time.time()
for i in range(len(words_list)):
  if (lettersum(words_list[i]) % 2) != 0:
    count += 1
print(" - There are", count, "words with an odd letter sum.")
end = time.time()
min_and_sec(start, end)

"""
print("\n 3. There are 1921 words with a letter sum of 100, making it the second most common letter sum. What letter sum is most common, and how many words have it?")
_100_count = 0
for i in range(len(words_list)):
  if lettersum(words_list[i]) == 100:
    _100_count += 1
print(" - There are", _100_count, "words with the letter sum of 100 as said above.")
start = time.time()
for i in range(1, len(words_list)):
  count = 0
  for j in range(len(words_list)):
    if lettersum(words_list[j]) == i:
      count += 1
    if count > _100_count:
      print(" - There are", count, "words with the letter sum", i, "which happens to be the most common letter sum.")
      break
  if count > _100_count:
    break
end = time.time()
min_and_sec(start, end)
"""

print("\n 4. zyzzyva and biodegradabilities have the same letter sum as each other (151), and their lengths differ by 11 letters. Find the other pair of words with the same letter sum whose lengths differ by 11 letters.")


print("\n 5. cytotoxicity and unreservedness have the same letter sum as each other (188), and they have no letters in common. Find a pair of words that have no letters in common, and that have the same letter sum, which is larger than 188. (There are two such pairs, and one word appears in both pairs.)")


print("\n 6. The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words. Each word in the list has both a different number of letters, and a different letter sum. The list is sorted both in descending order of word length, and ascending order of letter sum. What's the longest such list you can find?")