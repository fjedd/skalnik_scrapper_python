from deepdiff import DeepDiff

file1 = open('ekspresy.json' ,'r')
file2 = open('ekspresy_11_09_2022.json', 'r')

difference = DeepDiff(file1, file2)



print(f" ITEMS ADDED: {difference['values_changed']}\n")