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

    general_counts.print()

def print_lines_statistics_to_file(function_names, function_info):
    output_file = open("output.txt", 'w', encoding='utf-8')
    for i, name in enumerate(function_names):
        output_file.write(function_info[i].get_string_info(name[:-1]))
    output_file.close()

def count_lines_of_each_type(line_type_list):
    i = 0
    while line_type_list[i] != "function":
        i += 1

    line_info = []
    local_counts = CounterTypeLine()
    general_counts = CounterTypeLine()
    for line_type in line_type_list[i:]:
        if line_type == "function":
            line_info.append(local_counts)
            local_counts = CounterTypeLine()
        local_counts.increment_count(line_type)
        general_counts.increment_count(line_type)
    return line_info, general_counts

def plot_num_lines(function_info):
    num_code_lines = []
    for counts in function_info:
        num_code_lines.append(counts.get_count('code'))
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
    string_info = (f"{function_name}: \n         "
                   f"Number of lines: code: {counts_line_type['code']}, "
                   f"comments:  {counts_line_type['comment']}, "
                   f"blanks: {counts_line_type['blank']} \n")
    return string_info

class CounterTypeLine:
    def __init__(self):
        self.count = {
        'code': 0,
        'blank': 0,
        'comment': 0
    }

    def increment_count(self, line_type):
        if line_type == 'blank':
            self.count['blank'] += 1
        elif line_type == 'comment':
            self.count['comment'] += 1
        elif line_type == 'code' or 'function':
            self.count['code'] += 1

    def print(self):
        self.print_line_contribution('blank')
        self.print_line_contribution('comment')
        self.print_line_contribution('code')
        print ("Total lines: ", self.get_total_num_lines())

    def print_line_contribution(self, line_type):
        print (f"{line_type.capitalize()} lines: "
               f"{self.get_count(line_type)},"
               f" {self.get_line_contribution_percentage(line_type)}%")

    def get_line_contribution_percentage(self, line_type):
        return round(float(self.get_count(line_type) * 100) /
               self.get_total_num_lines(), 2)

    def get_count(self, name):
        return self.count[name]

    def get_string_info(self, name):
        string_info = (f"{name}: \n         "
                       f"code: {self.count['code']}, "
                       f"comments:  {self.count['comment']}, "
                       f"blanks: {self.count['blank']} \n")
        return string_info

    def get_total_num_lines(self):
        return (self.count['blank'] + self.count['comment'] +
                self.count['code'])

if __name__ == "__main__":
    main()











