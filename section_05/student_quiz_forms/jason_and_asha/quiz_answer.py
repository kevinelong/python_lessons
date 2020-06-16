raw_post = "q1001=B&q1002=A"

post_list = raw_post.split("&")
final_list = []
for item in post_list:
    parts = item.split("=")
    final_list.append({parts[0]: parts[1]})
print(final_list)

cooked_post = [
    {'q1001': 'B'},
    {'q1002': 'A'}
]
