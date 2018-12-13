with open("frequency.txt") as f:
  lines = [line.rstrip('\n') for line in f]

def first_dup():
  sum = 0
  frequencies_dict = set()
  frequencies_dict.add(0)
  duplicate= False
  while not duplicate:
    for line in lines:
      if line[0] == '+':
        sum += int(line[1:].strip())
      else:
        sum -= int(line[1:].strip())

      if sum in frequencies_dict:
        duplicate = True
        return sum
      else:
        frequencies_dict.add(sum)

print(first_dup())
