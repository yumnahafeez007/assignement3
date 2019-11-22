obj = {'a':2, 'b':5}

def is_key_present(x, dictionary):
  if x in dictionary:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')



is_key_present('a', obj)