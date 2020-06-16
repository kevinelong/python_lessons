
quiz_dict = {
    "author": "Kevin",
    "questions": [
        {
            "id": 1001,
            "text": "Which of the following is a fruit?",
            "answers": [
                {
                    "code": "A",
                    "text": "Banana",
                    "correct": False
                },
                {
                    "code": "B",
                    "text": "Strawberry",
                    "correct": True
                },
                {
                    "code": "C",
                    "text": "Tomato",
                    "correct": False
                },
                {
                    "code": "D",
                    "text": "Apple",
                    "correct": False
                }
            ],
            "correct": [
                "A",
                "B"
            ]
        },
        {
            "id": 1002,
            "text": "Is Portland weird?",
            "answers": [
                {
                    "code": "A",
                    "text": "Yes",
                    "correct" : True
                },
                {
                    "code": "B",
                    "text": "No",
                    "correct": False
                }
            ],
            "correct": [
                "B"
            ]
        }
    ]
}

top_part = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
    <style>
        form label {
            display: inline-block;
        }
    </style>
</head>
<body>

<h1>Quiz</h1>

<form method="post" action="evaluate.py">
    <fieldset>
        <legend>When and Who:</legend>
        <label>
            <h2>Date</h2>
            <input name="date_taken" type="date"><br/>
        </label>
        <label>
            <h2>Student Name</h2>
            <input name="student_name_first" placeholder="first">
            <input name="student_name_last" placeholder="last">
        </label>
    </fieldset>

    <hr>
"""

bottom_part = """
    <input type="submit">
</form>
</body>
</html>
"""


file_name = open("quiz_form_out.html","w")

file_name.write(top_part)
for q in quiz_dict["questions"]:
    file_name.write("<fieldset>")
    file_name.write("<legend>" + q["text"] + "</legend>")
    qid = str(q["id"])
    for a in q["answers"]:
        file_name.write('<p><label for="c1">')
        file_name.write('<input type="radio" name="q'
                +qid+'" id="'
                +a["code"]+'" value="'
                +a["code"]+'">')
        file_name.write(a["code"] + " " + a["text"])
        file_name.write('</label></p>')
    file_name.write("</fieldset>")
file_name.write(bottom_part)
file_name.close()

#POST = date_taken=2014-07-09&student_name_first=KKK&student_name_last=LLL&q1001=A&q1002=B
