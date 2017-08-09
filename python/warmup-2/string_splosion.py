''' Given a non-empty string like "Code" return a string like "CCoCodCode". '''

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
  s = ''
  for i in range(len(str)):
    s += str[:i]
  return s + str
