from collections import Counter

left_list = []
right_list = []

with open('input') as f:
  for line in f:
    left, right = map(int, line.split())

    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

print(left_list)
print(right_list)
print('------------------------------------')

right_count = Counter(right_list)

similarity = 0
for num in left_list:
  similarity += num * right_count[num]

print(similarity)