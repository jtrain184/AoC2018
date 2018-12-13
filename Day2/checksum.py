three_count = 0
two_count = 0
with open("input.txt") as f:
  for line in f:
    two_found = False
    three_found = False
    letter_count = {}
    for c in line:
      if c in letter_count:
        letter_count[c] = letter_count[c] + 1
      else:
        letter_count[c] = 1
    for key in letter_count.keys():
      if letter_count[key] == 3 and not three_found:
        three_count += 1
        three_found = True
      if letter_count[key] == 2 and not two_found:
        two_count += 1
        two_found = True

    print(letter_count)
    print(three_count)
    print(two_count)
checksum = three_count * two_count
print(checksum)
      