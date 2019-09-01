def add_string(str1):
  # If the length of the given string is less than 3, leave it unchanged.
  length = len(str1)
  if length<3:
      return str1
  # If the given string already ends with 'ing' then add 'ly'.
  suffix = "ing"
  if str1.endswith(suffix):
      str1 = str1+'ly'
  else:
      str1 = str1+'ing'
  # else: check last three letter of word and add -ing 

  
  return str1

str1="aing"
print(add_string(str1))