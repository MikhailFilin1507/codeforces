
num_sets = int(input())

days_list = []
ids_list = []

for n in range(num_sets):

    days = int(input())
    days_list.append(days)

    id_str = input()
    ids = [int(item) for item in id_str.split()]
    ids_list.append(ids)

for n in range(len(days_list)):
    unique_ids = [ids_list[n][0]]
    answer = 'YES'
    for m in range(1, days_list[n]):
        if ids_list[n][m] in unique_ids and ids_list[n][m] != ids_list[n][m-1]:
            answer = 'NO'
            break
        elif ids_list[n][m] not in unique_ids:
            unique_ids.append(ids_list[n][m])
    print(answer)








# #записываем входные данные
# for n in range(num_sets):
#     input() #принимаем пустую строку
#
#     dimension_string = input()
#     dimension_list_loc = [int(item) for item in dimension_string.split()]
#     dimension_list_gen.append(dimension_list_loc)
#
#     array_list=[]
#     for i in range(dimension_list_loc[0]):
#         string = input()
#         str_list = [int(item) for item in string.split()]
#         array_list.append((str_list))
#     array_list_gen.append(array_list)
#
#     click = int(input())
#     num_clicks.append(click)
#
#     columns = input()
#     columns_list = [int(item) for item in columns.split()]
#     columns_list_gen.append(columns_list)
#
# for n in range(len(num_clicks)):
#     for k in columns_list_gen[n]:
#         N = len(array_list_gen[n])
#         for bypass in range(1,N):
#             for m in range(0, N-bypass):
#                 if array_list_gen[n][m][k-1] > array_list_gen[n][m+1][k-1]:
#                     array_list_gen[n][m], array_list_gen[n][m+1] = array_list_gen[n][m+1], array_list_gen[n][m]
#
#
# for n in range(len(array_list_gen)):
#     for m in range(len(array_list_gen[n])):
#         for k in range(len(array_list_gen[n][m])):
#             if k < len(array_list_gen[n][m])-1:
#                 print(array_list_gen[n][m][k], end=' ')
#             else:
#                 print(array_list_gen[n][m][k])
#     print()