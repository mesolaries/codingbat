''' Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). '''

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
  if len(str) < 2:
    return 0
  count = 0
  last2 = str[-2:]
  for i in range(len(str) - 2):
    if str[i:i+2] == last2:
      count += 1
  return count
