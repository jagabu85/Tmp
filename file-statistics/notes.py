print("################### DEBUG: start")

def print_functions_line_counts(line_counts_list):
    print(line_counts_list)
    return

#input_file_2 = open("kernel.py", mode='r', encoding='utf-8')



input_file_2 = open("kernel.py", mode='r', encoding='utf-8')
function = input_file_2.readlines()[functions_starting_lines[0]]

for i, _ in enumerate(functions_starting_lines[:-1]):
    print(function)
    function = input_file_2.readlines()[0:functions_starting_lines[i]]
    line_counts = count_lines_of_each_type(function)
    input_file_2.seek(0)


for i, _ in enumerate(functions_starting_lines[:-1]):
    function = input_file_2.readlines()[functions_starting_lines[i]:
                                        functions_starting_lines[i+1]]
    line_counts = count_lines_of_each_type(function)
    input_file_2.seek(0)

print("################### DEBUG: end")


a = input_file_2.readlines()[functions_starting_lines[
                                   0]:functions_starting_lines[1]]
print("Starting: ", functions_starting_lines[0])
print("starting next: ", functions_starting_lines[1])
print(a[:])
line_counts = count_lines_of_each_type(a)
print_line_counts(line_counts)
input_file_1.close()

#print(input_file_2.readlines()[functions_starting_lines[1]:functions_starting_lines[2]])



"""
functions_line_counts =[]
for file_string in :
    functions_line_counts.append(count_lines_of_each_type(file_string))
print_functions_line_counts(functions_line_counts)
input_file_2.close()
print("################### DEBUG: end")"""


#for i, line in enumerate(input_file_2):
#    if i < 10:
#        print(line[:-1])

"""
input_file = open("kernel.py", mode='r', encoding='utf-8')
text_file = open("output.txt", 'w', encoding='utf-8')
text_file.write(input_file.read())
input_file.close()
text_file.close()
"""