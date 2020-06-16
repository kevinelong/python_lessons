raw_post = "date_taken=2014-07-03&student_name_first=David&student_name_last=Streckert&1=T&2=Y"
post_list = raw_post.split("&")
final_list = []
for item in post_list:
    parts = item.split("=")
    final_list.append({parts[0]: parts[1]})
print(final_list)

cooked_post = [
    {'date_taken': '2014-07-03'},
    {'student_name_first': 'David'},
    {'student_name_last': 'Streckert'},
    {'1': 'T'},
    {'2': 'Y'}
]
