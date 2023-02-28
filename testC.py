
num_sets = int(input())

gen_list = []
#принимаем на вход значение и формируем список словарей
for n in range(num_sets):
    dict={}
    dev_num = int(input())
    qual = input()
    list_qual = qual.split()
    for i in range(len(list_qual)):
        list_qual[i] = int(list_qual[i])
        dict[i+1] = list_qual[i]
    gen_list.append(dict)
#print(gen_list)

gen_list2 = []
for n in range(len(gen_list)):

    dict_red=[] #список для списков пар
    lst1 = [] #список использованных ключей в наборе

    for k, v in gen_list[n].items():
        #print(k)
        if k not in lst1:
            #print(k, k not in lst1)

            lst1.append(k) #добавляем номер в lst1
            dict_razn={} #создаем словарь с модулями разницы

            if len(lst1) == len(gen_list[n])-1: #для последнего
                for key in gen_list[n].keys():
                    if key not in lst1:
                        dict_red.append([k, key])
            else:

                for key, value in gen_list[n].items(): #цикл наполнения словаря с разницами
                    if key != k and key not in lst1:
                        dict_razn[key] = abs(v - value)
                #print(dict_razn)


                i=0 #счетчик, чтобы один раз добавить пару

                for e, a in dict_razn.items():
                    if a == min(dict_razn.values()) and i == 0 and e not in lst1:
                        #print(k)
                        lst1.append(e)
                        dict_red.append([k, e])
                        i += 1
                        #print(f' {lst1} -------- {dict_red}')
    gen_list2.append(dict_red)

for n in range(len(gen_list2)):
    for m in range(len(gen_list2[n])):
        print(gen_list2[n][m][0], gen_list2[n][m][1])
    print()