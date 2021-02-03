import codecs
import numpy as np
import matplotlib.pyplot as plt

def count_lines_of_each_type(line_type_list):

    counts = {
        "code": 0,
        "blank": 0,
        "comment": 0
    }

    line_info = []
    i = 0
    while line_type_list[i] != "function":
        i += 1

    for line_type in line_type_list[i:]:
        if line_type == "function":
            line_info.append(counts.copy())
            counts["blank"] = 0
            counts["comment"] = 0
            counts["code"] = 0
        else:
            if line_type == "blank":
                counts["blank"] += 1
            elif line_type == "comment":
                counts["comment"] += 1
            elif line_type == "code":
                counts["code"] += 1

    return line_info

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
    if line[0] == "#":
        return True
    else:
        return False

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

def get_function_names(file):

    function_names = []
    for i, line in enumerate(file):
        if line[0:3] == "def":
            function_names.append(line[4:])

    return function_names

def get_string_line_statistics(function_name, counts_line_type):
    string_info = (f"{function_name[:-1]}: \n         "
                   f"code: {counts_line_type['code']}, "
                   f"comments:  {counts_line_type['comment']}, "
                   f"blanks: {counts_line_type['blank']} \n")
    return string_info

def main():
    input_file = open("kernel.py", mode='r', encoding='utf-8')
    function_names = get_function_names(input_file)
    input_file.seek(0)
    line_types = classify_lines(input_file)


    function_info = count_lines_of_each_type(line_types)

    output_file = open("output.txt", 'w', encoding='utf-8')
    for i, name in enumerate(function_names):
        output_file.write(get_string_line_statistics(function_names[i], function_info[i]))
        print(i)
    output_file.close()

    print(function_info)

if __name__ == "__main__":
    main()











