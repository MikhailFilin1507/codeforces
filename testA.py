
a = int(input())
lst1 = []

for i in range(a):
    num = input()
    lst2 = num.split()
    lst2[0] = int(lst2[0])
    lst2[1] = int(lst2[1])
    lst1.append(lst2)

for i in range(len(lst1)):
    print(lst1[i][0] + lst1[i][1])
