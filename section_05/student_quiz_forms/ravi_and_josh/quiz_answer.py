raw_post = "date_taken=2014-07-25&student_name_first=Ravi&student_name_last=Prasad+Nandikanti&g1=1&g2=2"
post_list = raw_post.split("&")
final_list = []
for item in post_list:
    parts = item.split("=")
    final_list.append({parts[0]: parts[1]})
print(final_list)

cooked_answer = [
    {'date_taken': '2014-07-25'},
    {'student_name_first': 'Ravi'},
    {'student_name_last': 'Prasad+Nandikanti'},
    {'g1': '1'},
    {'g2': '2'}
]
