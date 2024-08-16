l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

new_list = []
longer_list = l1 if len(l1) > len(l2) else l2
shorter_list = l2 if len(l2) < len(l1) else l1
leftover = 0
for i in range(1, len(shorter_list) + 1):
    temp = longer_list[-i] + shorter_list[-i] + leftover
    if temp > 9:
        leftover = temp // 10
        temp = temp % 10
    else:
        leftover = 0
    new_list.append(temp)
if longer_list != shorter_list:
    for i in range(len(shorter_list) + 1, len(longer_list) + 1):
        temp = longer_list[-i] + leftover
        if temp > 9:
            leftover = temp // 10
            temp = temp % 10
        else:
            leftover = 0
        new_list.append(temp)

if leftover > 0:
    new_list.append(leftover)
print(new_list)