def palindrome (array):
  min = 0
  max = len(array) - 1

  while True:

    if min > max:
      return True