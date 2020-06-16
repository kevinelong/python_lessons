f = open("quiz_output.html", "w")

f.write("""
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
<form method="post" action="evaluate.py">
""")


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

for q in quiz_dict["questions"]:
    f.write("<fieldset>\n<legend>" + (q["text"]) + "</legend>")
    q_number = str(q["id"])
    for a in q["answers"]:
        f.write("<p><label for=" + a["code"] + "><input type= radio name= q" + q_number + 
            " id=" + a["code"] + " value=" + a["code"] + ">" + a["text"] + "</label></p>")
    f.write("</fieldset>")

f.write("\n<input type='submit'> \n</form> \n</body>\n </html>")

f.close()

