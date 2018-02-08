
def write_list_to_file(text_list, file_name):
    output_file = open(file_name, "w")
    output_file.write("\n".join(text_list))
    output_file.close()

def read_list_from_file(file_name):

    input_file = open("data.txt", "r")
    line_list = input_file.readlines()
    output_word_list = []
    input_file.close()

    for w in line_list:
        output_word_list.append(w.strip())

    return output_word_list


print output_word_list

assert word_list == output_word_list
