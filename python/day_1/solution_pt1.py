left_list = []
right_list = []

with open('input') as f:
  for line in f:
    left, right = map(int, line.split())

    left_list.append(left)
    right_list.append(right)

print(left_list)
print(right_list)
print('------------------------------------')
left_list.sort()
right_list.sort()

print(left_list)
print(right_list)
print('------------------------------------')

sum = 0

for i in range(len(left_list)):
  sum += abs(left_list[i]-right_list[i])

print('sum = ' + str(sum))