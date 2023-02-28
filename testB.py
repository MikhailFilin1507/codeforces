
num_sets = int(input())

gen_list = []

for n in range(num_sets):
    num_prod = int(input())
    prices = input()
    list_prices = prices.split()
    for i in range(len(list_prices)):
        list_prices[i] = int(list_prices[i])
    list_prices.sort()
    gen_list.append(list_prices)

gen_list_red = []

for n in range(len(gen_list)):
    gen_set = set(gen_list[n])
    gen_list_red.append([])
    a=0
    for l in gen_set:
        gen_list_red[n].append([])
        for k in range(len(gen_list[n])):
            if gen_list[n][k] == l:
                gen_list_red[n][a].append(gen_list[n][k])
        a+=1

for n in range(len(gen_list_red)):
    sum_n = 0
    for k in range(len(gen_list_red[n])):
        len_k = len(gen_list_red[n][k])
        if len_k % 3 == 0:
            sum_k = (len_k // 3) * 2 * gen_list_red[n][k][0]
        else:
            sum_k = (len_k // 3 * 2 * gen_list_red[n][k][0]) + (len_k % 3 * gen_list_red[n][k][0])
        sum_n += sum_k
    print(sum_n)












