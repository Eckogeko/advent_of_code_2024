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

similarity = 0
l = 0
r = 0
count = 0
repeat = 0
while l <(len(left_list)):
  print('l counter is ' + str(l))
  print('r counter is ' + str(r))
  if l>=(len(left_list)) or r>=(len(right_list)):
    break

  elif (left_list[l] < right_list[r] and repeat != left_list[l]):
    l += 1
    count = 0
    print("L + 1")
    continue

  elif left_list[l] == right_list[r] and repeat == left_list[l]:
    repeat = left_list[l]
    count += 1
    r += 1
    print("R + 1")

  elif left_list[l] == right_list[r] and repeat != left_list[l]:
    repeat = left_list[l]
    count = 1
    r += 1
    print("R + 1")

  elif left_list[l] < right_list[r] and repeat == left_list[l]:
    similarity += (count * left_list[l])
    print("similarity = " + str(similarity))
    l += 1
  else:
    print('left list is = ' + str(left_list[l]))
    print('right list is = ' + str(right_list[r]))
print('similarity = ' + str(similarity))