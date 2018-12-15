lines = []
with open("input.txt") as f:
    for line in f:
        lines.append(line.strip())


def differ_by_one():
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            common_chars = []
            for k in range(len(lines[i])):
                if lines[i][k] == lines[j][k]:
                    common_chars.append(lines[i][k])
            if len(common_chars) == len(lines[i]) - 1:
                return common_chars

print(lines)
result = differ_by_one()
print(''.join(result))