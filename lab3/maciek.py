def palindrome (array):
  min = 0
  max = len(array) - 1

  while True:

    if min > max:
      return True

    a = array[min]
    b = array[max]

    if a != b:
      return False;

    min += 1
    max -= 1

words = ["Oxo", "OXO", "123454321", "ROTATOR", "12345	54321", "omg"]

for line in words:
  if palindrome(line):
    print("Palindrome yey:    ", line)
  else:
    print("Not palindrome:", line)

