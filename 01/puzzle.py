
def puzzle1(lines):
    max = 0
    sum = 0

    for line in lines:
        if line.strip() == '':
            sum = 0
        else:    
            num = int(line)
            sum += num
            if sum > max:
                max = sum

    return max

def puzzle2(lines):
    sum = 0
    sums = set()

    for line in lines:
        if line.strip() == '':
            sums.add(sum)
            sum = 0
        else:    
            num = int(line)
            sum += num
    
    sums.add(sum)
    # sort sums
    sums = sorted(sums, reverse=True)

    return sums[0] + sums[1] + sums[2]


with open('/Users/nicksologoub/_src_/AdventOfCode2022/01/input.txt') as f:
  lines = f.readlines()

p1 = puzzle1(lines)
p2 = puzzle2(lines)

print(p1)
print(p2)