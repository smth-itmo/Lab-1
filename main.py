# флаг
# RED = '\u001b[41m'
# BLUE = '\u001b[44m'
# WHITE = '\u001b[47m'
# END = '\u001b[0m'
# BLACK = '\u001b[30m'


# print(f'{WHITE}{"  " * (6)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (6)}{END}')
# print(f'{WHITE}{"  " * (4)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (1)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (4)}{END}')
# print(f'{WHITE}{"  " * (3)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (3)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (3)}{END}')
# print(f'{WHITE}{"  " * (2)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (5)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (2)}{END}')
# print(f'{WHITE}{"  " * (1)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (7)}{END}', f'{BLACK}{"  " * (2)}{END}', f'{WHITE}{"  " * (1)}{END}')




# узор
# pattern = [
#     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0]
#     [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
#     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
# ]
 
# res = ''

# for row in pattern:
#     for cell in row:
#         if cell:
#             res += f"{BLACK}  {END}"
#         else:
#             res += f"{WHITE}  {END}"
#     res += "\n"

# print(res)

# функция
# plot_list = [[0 for i in range(10)] for i in range(10)]
# result = [0 for i in range(10)]

# for i in range(10):
#     result[i] = 1 / (i + 1)

# step = round(abs(result[0] - result[9]) / 9, 2)
# print(step)

# for i in range(10):
#     for j in range(10):
#         if j == 0:
#             plot_list[i][j] = step * (8 - i) + step

# for i in range(9):
#     for j in range(10):
#         if abs(plot_list[i][0] - result[9 - j]) < step:
#             for k in range(9):
#                 if 8 - k == j:
#                     plot_list[i][k + 1] = 1

# for i in range(9):
#     line = ''
#     for j in range(10):
#         if j == 0:
#             line += '\t' + str(round(plot_list[i][j], 2)) + '\t'
#         if plot_list[i][j] == 0:
#             line += '--'
#         if plot_list[i][j] == 1:
#             line += '**'
#     print(line)
# print('\t0\t1 2 3 4 5 6 7 8 9')


# 4 задание
# numbers_list = []

# with open('sequence.txt', 'r') as file:
#     for line in file:
#         number = float(line)
#         if number > 0 and number != 5:
#             numbers_list.append(number)

# print(numbers_list)