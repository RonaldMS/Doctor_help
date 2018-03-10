from openpyxl import load_workbook
wb = load_workbook('test.xlsx').active
alph = "ABCDEFGHIJKJMNOPQRSTUVWXYZ"
number_it = 1
alph_it = 0
data = dict()
while number_it != 158:
    data[number_it-1] = list()
    data[number_it-1].append(wb['B' + str(number_it)].value)
    while alph[alph_it] != 'V':
        if wb[alph[alph_it] + str(number_it)].value == None:
            data[number_it - 1].append('-')
        else:
            data[number_it-1].append(wb[alph[alph_it] + str(number_it)].value)
        alph_it += 1
    number_it += 1
    alph_it = 0
with open('data.txt', 'w') as file:
    print(data, file=file)