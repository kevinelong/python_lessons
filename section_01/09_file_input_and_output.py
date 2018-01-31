word_list = ["hello", "world"]
output_file = open("data.txt", "w")
output_file.write("\n".join(word_list))
output_file.close()

input_file = open("data.txt", "r")
line_list = input_file.readlines()
output_word_list = []
input_file.close()
for w in line_list:
    output_word_list.append(w.strip())
print output_word_list
