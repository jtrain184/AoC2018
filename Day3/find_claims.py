claims = []
with open('input.txt') as f:
  for line in f:
    line_split = line.split()
    id = line_split[0].split('#')[1]
    position = line_split[2].split(',')
    position_col = position[0]
    position_row = ''.join([s for s in position[1] if s.isdigit()])
    size = line_split[3].split('x')
    width = size[0]
    height = size[1]
    temp = (position_col, position_row, width, height, id)
    claims.append(temp)

w, h = 1100, 1100;
Matrix = [[0 for x in range(w)] for y in range(h)] 
overlap = 0

# Part 1
for claim in claims:
  start_col, start_row = int(claim[0]), int(claim[1])
  width, height = int(claim[2]), int(claim[3])
  for i in range(start_row + 1, start_row + height + 1):
    for j in range(start_col + 1, start_col + width + 1):
      if Matrix[i][j] != 1:
        Matrix[i][j] += 1
      else:
          Matrix[i][j] += 1
          overlap += 1

# Part 2
for claim in claims:
  start_col, start_row = int(claim[0]), int(claim[1])
  width, height = int(claim[2]), int(claim[3])
  ok = True
  for i in range(start_row + 1, start_row + height + 1):
    for j in range(start_col + 1, start_col + width + 1):
      if Matrix[i][j] > 1:
        ok = False
  if ok:
    print(claim[4])
