import os
import string

def split_string(s):
  # Calculate the length of the string
  n = len(s)
  
  # Check if the length of the string is even
  if n % 2 == 0:
    # If the length is even, split the string into two equal halves
    first_half = s[:n//2]
    second_half = s[n//2:]
  else:
    # If the length is odd, split the string into two halves with the first half being one character longer
    first_half = s[:n//2 + 1]
    second_half = s[n//2 + 1:]
  
  # Return the two halves as a tuple
  return (first_half, second_half)

def get_priority(s):
    return priorities.index(s)+1

def puzzle1(lines):
    sum = 0
    for line in lines:
        parts = split_string(line.strip())
        part1 = parts[0]
        part2 = parts[1]
        for part in part1:
            if part in part2:
                part2 = part2.replace(part, '')
                priority = get_priority(part)
                sum += priority
    return sum

def puzzle2(lines):
    sum = 0
    i = 0
    for line in lines:
        if i == 0:
            set1 = set(line.strip())
        elif i == 1:
            set2 = set(line.strip())
        else:
            set3 = set(line.strip())
            commonSet = set1 & set2 & set3
            common = commonSet.pop()
            sum += get_priority(common)
            i = -1
        
        i += 1

    return sum

# Get the current working directory
cwd = os.getcwd()

with open(os.getcwd() + '/03/input.txt') as f:
  lines = f.readlines()

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
priorities = lowercase + uppercase

p1 = puzzle1(lines)
p2 = puzzle2(lines)

print(p1)
print(p2)        
