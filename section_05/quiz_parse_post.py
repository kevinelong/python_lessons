raw_post = "date_taken=2014-07-09&student_name_first=KKK&student_name_last=LLL&q1001=C&q1002=B"

post_list = raw_post.split("&")
final_list = []
for item in post_list:
    parts = item.split("=")
    final_list.append({parts[0]: parts[1]})
print(final_list)

#
# for item in final_list:
#     for k in item.keys():
#         print(k + " = " + item[k])
#
#
# cooked_post_list = [
#     {'date_taken': '2014-07-09'},
#     {'student_name_first': 'KKK'},
#     {'student_name_last': 'LLL'},
#     {'q1001': 'C'},
#     {'q1002': 'B'}
# ]
