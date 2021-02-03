import codecs
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def main():
    input_file = open("kernel.py", mode='r', encoding='utf-8')
    function_names = get_function_names(input_file)

    input_file.seek(0)
    line_types = classify_lines(input_file)
    function_info, general_counts = count_lines_of_each_type(line_types)

    print_lines_statistics_to_file(function_names, function_info)

    plot_num_lines(function_info)

    print(general_counts)


def print_lines_statistics_to_file(function_names, function_info):
    output_file = open("output.txt", 'w', encoding='utf-8')
    for i, name in enumerate(function_names):
        output_file.write(
            get_string_line_statistics(function_names[i], function_info[i]))
    output_file.close()

def count_lines_of_each_type(line_type_list):
    i = 0
    while line_type_list[i] != "function":
        i += 1

    line_info = []
    local_counts = create_counts()
    general_counts = create_counts()
    for line_type in line_type_list[i:]:
        if line_type == "function":
            line_info.append(local_counts)
            local_counts = create_counts()
        increment_count(local_counts, line_type)
        increment_count(general_counts, line_type)
    return line_info, general_counts

def increment_count(count, line_type):
    if line_type == "blank":
        count["blank"] += 1
    elif line_type == "comment":
        count["comment"] += 1
    elif line_type == "code" or "function":
        count["code"] += 1

def create_counts():
    count = {
        "code": 0,
        "blank": 0,
        "comment": 0
    }
    return count

def plot_num_lines(function_info):
    num_code_lines = []
    for counts in function_info:
        num_code_lines.append(counts['code'])
    plt.plot(num_code_lines)
    plt.xlabel('ID method')
    plt.ylabel('# of lines / method')
    plt.show()

def get_function_names(file):
    function_names = []
    for i, line in enumerate(file):
        if line[0:3] == "def":
            function_names.append(line[4:])

    return function_names

def classify_lines(file):
    lines_type =[]
    for i, line in enumerate(file):
        if is_blank(line):
            lines_type.append("blank")
        elif is_function_def(line):
            lines_type.append("function")
        elif is_comment(line):
            lines_type.append("comment")
        else:
            lines_type.append("code")

    return lines_type

def is_blank(line):
    if line == "\n":
        return True
    else:
        return False

def is_function_def(line):
    if line[0:3] == "def":
        return True
    else:
        return False

def is_comment(line):
    for current_char in line:
        if current_char == "#":
            return True
        elif current_char == '\t' or current_char == ' ':
            None
        else:
            return False
    return False

def get_string_line_statistics(function_name, counts_line_type):
    string_info = (f"{function_name[:-1]}: \n         "
                   f"code: {counts_line_type['code']}, "
                   f"comments:  {counts_line_type['comment']}, "
                   f"blanks: {counts_line_type['blank']} \n")
    return string_info

if __name__ == "__main__":
    main()











