with open("list1.txt", "r") as list1_file:
    list1 = list1_file.readlines()

with open("list2.txt", "r") as list2_file:
    list2 = list2_file.readlines()

overlap = [int(n) for n in list1 if n in list2]

print(overlap)
