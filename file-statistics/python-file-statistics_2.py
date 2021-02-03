import codecs
import numpy as np
import matplotlib.pyplot as plt

def count_lines_of_each_type(file):
    """ Cound the lines of a file by clasification (code, blank or comment).
    :param file: text file
    :type file: <class '_io.TextIOWrapper'>

    :return counts: Contain three integers with the keys: blank, comment and
    ode.
    :type counts: dictionary
    """
    counts = {
        "code": 0,
        "blank": 0,
        "comment": 0
    }

    for line in file:
        if line == "\n":
            counts['blank'] += 1
        elif line[0] == "#":
            counts['comment'] += 1
        else:
            counts['code'] += 1

    return counts

def print_line_counts(counts):
    print_line_contribution('blank', counts)
    print_line_contribution('comment', counts)
    print_line_contribution('code', counts)

    print ("Total lines: ",sum(counts.values()))

    return

def print_line_contribution(line_type, line_info):
    print (f"{line_type.capitalize()} lines: {line_info[line_type]},", \
           f"{round(float(line_info[line_type] * 100) / sum(line_info.values()), 2)}%")
    return

def get_lines_functions_starts(file):
    """ Get a list with the number of line where each function starts
    :param file: text file
    :type file: <class '_io.TextIOWrapper'>

    :return function_starting_lines:List with the number of line where each
    function starts
    :type list
    """

    function_starting_lines =[]
    for i, line in enumerate(file):
        if line[0:3] == "def":
            function_starting_lines.append(i)

    return function_starting_lines

def plot_num_lines(function_size):
    plt.plot(function_size)
    plt.xlabel('ID method')
    plt.ylabel('# of lines / method')
    plt.show()

def main():
    print("############################# Line types ")
    input_file_1 = open("kernel.py", mode='r', encoding='utf-8')
    line_counts = count_lines_of_each_type(input_file_1)
    print_line_counts(line_counts)
    input_file_1.close()

    print("############################# Chart number of lines ")
    input_file_2 = open("kernel.py", mode='r', encoding='utf-8')
    functions_starting_lines = np.array(get_lines_functions_starts(input_file_2))
    functions_size = functions_starting_lines[1:] - functions_starting_lines[0:-1]
    input_file_2.close()
    #plot_num_lines(functions_size)


    input_file_2 = open("kernel.py", mode='r', encoding='utf-8')

    text_file = open("output.txt", 'w', encoding='utf-8')
    input_file_2.seek(0)
    functions_statistics = []
    for i, _ in enumerate(functions_starting_lines[:-1]):
        function = input_file_2.readlines()[functions_starting_lines[i]:
                                            functions_starting_lines[i + 1]]
        line_counts = count_lines_of_each_type(function)
        functions_statistics.append(line_counts)
        input_file_2.seek(0)
    text_file.close()
    input_file_2.close()

    print(functions_statistics)

if __name__ == "__main__":
    main()








